#!

import getopt, sys, time

def main():
    num_users = str(sys.argv[1])
    web_ip = str(sys.argv[2])
    print('Running Test against ' + web_ip + ' with ' + num_users + ' user thread(s).')
    time.sleep(30)
    print('Done Running Test')

if __name__ == "__main__":
    main()
