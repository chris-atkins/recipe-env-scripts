#!

import getopt, sys, time, requests

def main():
    num_users = str(sys.argv[1])
    web_ip = str(sys.argv[2])
    print('Running Test against ' + web_ip + ' with ' + num_users + ' user thread(s).')
    url = 'http://' + web_ip + ':8000/api/recipe'
    for i in xrange(10):
        time.sleep(3)
        requests.get(url, headers={})

    print('Done Running Test')

if __name__ == "__main__":
    main()
