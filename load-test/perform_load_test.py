#!
import os
import time
import requests

token = os.environ['TOKEN']
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
web_ip = os.environ['WEB_IP']
number_of_servers = os.environ['NUMBER_OF_TEST_SERVERS']
number_of_users = os.environ['NUMBER_OF_SIMULATED_USERS_PER_SERVER']
time_to_run_in_seconds = os.environ['TIME_TO_RUN_IN_SECONDS']
cert_path = os.environ['CERT_PATH']
workspace = os.environ['WORKSPACE']

def create_new_server(server_name):
    post_data={"name":server_name,"region":"nyc3","size":"1gb","image":"docker","ssh_keys":["1734160"],"backups":False,"ipv6":False,"user_data":None,"private_networking":None}
    new_server_response = requests.post('https://api.digitalocean.com/v2/droplets', json=post_data, headers=headers);
    print('Build server ' + server_name + ' responded with ' + str(new_server_response.status_code))

def wait_until_all_servers_are_ready():
    all_servers_ready = False
    while all_servers_ready == False:
        getDropletsResponse = requests.get('https://api.digitalocean.com/v2/droplets?page=1&per_page=50', headers=headers)
        all_servers_ready = True
        for droplet in getDropletsResponse.json()['droplets']:
            if all_servers_ready == True and droplet['status'] != 'active':
                all_servers_ready = False
                print('Waiting for droplet ' + str(droplet['name']) + '(' + droplet['status'] + ')')
        if all_servers_ready == False:
            time.sleep(5)
    print('All load test runner servers are ready to go!')

def create_test_servers(number_of_servers):
    for i in xrange(int(number_of_servers)):
        server_name = 'LOAD-TEST-RUNNER-' + str(i)
        create_new_server(server_name=server_name)
    wait_until_all_servers_are_ready()

def find_droplet_public_ip(droplet):
    networks = droplet['networks']['v4']
    for network in networks:
        if network['type'] == 'public':
            return network['ip_address']

def find_load_test_server_ips():
    ip_addresses = []
    getDropletsResponse = requests.get('https://api.digitalocean.com/v2/droplets?page=1&per_page=50', headers=headers)
    allDroplets = getDropletsResponse.json()['droplets']
    for droplet in allDroplets:
        name = droplet['name']
        if name.startswith('LOAD-TEST-RUNNER'):
            ip = find_droplet_public_ip(droplet=droplet)
            ip_addresses.append(ip)
            print('Found IP for server ' + name + ': ' + ip)
    return ip_addresses

def deploy_code_to_servers(server_ips):
    time.sleep(25)
    print('deploying code to servers')
    for ip in server_ips:
        print('deploying to ' + ip)
        command = 'scp -r -o StrictHostKeyChecking=no -i ' + cert_path + ' ' + workspace + '/load-test/run_load_test.py' + ' root@' + ip + ':/root/run_load_test.py'
        print('Running command: ' + command)
        os.system(command)

def start_testing_on_all_servers(server_ips):
    time.sleep(5)
    print('starting testing on all servers')
    for ip in server_ips:
        command = 'ssh  -i ' + cert_path + ' root@' + ip + ' "python /root/run_load_test.py ' + number_of_users + ' ' + web_ip + ' > log.txt 2> error.txt &"'
        print('Running command: ' + command)
        os.system(command)

def end_testing_when_time_expires(time_to_run_in_seconds):
    time.sleep(float(time_to_run_in_seconds))
    droplets = {}
    getDropletsResponse = requests.get('https://api.digitalocean.com/v2/droplets?page=1&per_page=100', headers=headers)
    for droplet in getDropletsResponse.json()['droplets']:
        name = str(droplet['name'])
        id = str(droplet['id'])
        droplets[id] = name
    for id in droplets.keys():
        name = droplets[id]
        if name.startswith('LOAD-TEST-RUNNER'):
            print('Deleting: ' + name + ' | ' + id)
            deleteResponse = requests.delete('https://api.digitalocean.com/v2/droplets/' + id, headers=headers)
            print('Status ' + str(deleteResponse.status_code))




print('Running Load Test against ' + web_ip + ' with ' + number_of_servers + ' servers, each simulating ' + number_of_users + ' users.')
create_test_servers(number_of_servers=number_of_servers)
server_ips = find_load_test_server_ips()
deploy_code_to_servers(server_ips=server_ips)
start_testing_on_all_servers(server_ips=server_ips)
end_testing_when_time_expires(time_to_run_in_seconds=time_to_run_in_seconds)
print('Done running Load Test - remember to delete the grafana container after inspecting the results.')
