#!
import requests
import os
import time

print('Start building test environments')

token = os.environ['TOKEN']
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

def create_new_server(server_name):
    post_data={"name":server_name,"region":"nyc3","size":"1gb","image":"docker","ssh_keys":["1734160"],"backups":False,"ipv6":False,"user_data":None,"private_networking":None}
    new_server_response = requests.post('https://api.digitalocean.com/v2/droplets', json=post_data, headers=headers);
    print('Build server ' + server_name + ' responded with ' + str(new_server_response.status_code))
    print(new_server_response.text)
    return str(new_server_response.json()['droplet']['id'])


test_recipe_service_id = create_new_server(server_name='TEST-ENV-RECIPE-SERVICE')
test_recipe_web_id = create_new_server(server_name='TEST-ENV-RECIPE-WEB')


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
print('All droplets are ready to go!')

test_recipe_service_ip = ''   
test_recipe_web_ip = ''   
for droplet in getDropletsResponse.json()['droplets']:
    ip = str(droplet['networks']['v4'][0]['ip_address'])
    ip_type = str(droplet['networks']['v4'][0]['type'])
    id = str(droplet['id'])
    if id == test_recipe_service_id:
        test_recipe_service_ip = ip
        
    if id == test_recipe_web_id:
        test_recipe_web_ip = ip
        
    print(str(droplet['name']) + ' | ' + id + ' | ' + ip + ' ' + ip_type)

test_recipe_service_ip        
file = open('env.props', 'w')
file.write('TEST=hi, its me!\n')
file.write('SERVICE_IP=' + test_recipe_service_ip + '\n')
file.write('WEB_IP=' + test_recipe_web_ip + '\n')
file.close()
print('done creating file')

print('Done building test environments')