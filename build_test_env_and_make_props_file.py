#!
import requests
import os
import time

print('Start building test environments')

token = os.environ['TOKEN']
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

def create_new_server(server_name):
    post_data={"name":server_name,"region":"nyc3","size":"1gb","image":"docker","ssh_keys":["1734092"],"backups":False,"ipv6":False,"user_data":None,"private_networking":None}
    new_server_response = requests.post('https://api.digitalocean.com/v2/droplets', json=post_data, headers=headers);
    print('Build server ' + server_name + ' responded with ' + str(new_server_response.status_code))
    return str(droplet['networks']['v4'][0]['ip_address'])


test_recipe_ip = create_new_server(server_name='TEST-ENV-RECIPE-SERVICE')
# create_new_server(server_name='TEST-ENV-RECIPE-WEB')


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
for droplet in getDropletsResponse.json()['droplets']:
    print(str(droplet['name']) + ' | ' + str(droplet['id']) + ' | ' + str(droplet['networks']['v4'][0]['ip_address']) + ' ' + str(droplet['networks']['v4'][0]['type']))
        
file = open('env.props', 'w')
file.write('TEST=hi, its me!\n')
file.write('SSH_HOSTNAME=' + test_recipe_ip + '\n')
file.close()
print('done creating file')

print('Done building test environments')