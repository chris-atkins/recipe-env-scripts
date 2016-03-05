#!
import requests
import os

print('Start deleting test environments')

token = os.environ['TOKEN']
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
getDropletsResponse = requests.get('https://api.digitalocean.com/v2/droplets?page=1&per_page=50', headers=headers)

droplets = {}
for droplet in getDropletsResponse.json()['droplets']:
    name = str(droplet['name'])
    id = str(droplet['id'])
    droplets[id] = name 
    
for id in droplets.keys():
    name = droplets[id]
    if name.startswith('TEST-ENV'):
        print('Deleting: ' + name + ' | ' + id)
        deleteResponse = requests.delete('https://api.digitalocean.com/v2/droplets/' + id, headers=headers)


print('Done deleting test environments')