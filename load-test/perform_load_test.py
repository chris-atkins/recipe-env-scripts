#!
import os

web_ip = os.environ['WEB_IP']
print('Running Load Test at ' + web_ip)



print('Done running Load Test - remember to delete the grafana container after inspecting the results.')