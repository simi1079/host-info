import sys
from .lib import update_host, usage, search_hosts
from .exceptions import InvalidIP, InvalidHostname

INPUTFILE = "./hostsfile.txt"


def main():
    cmd_args = ["-r", "-w", ]
    args = sys.argv[1:]

    if len(args) == 0 or args[0] == '-h' or args[0] not in cmd_args:
        usage()
        return

    if args[0] == '-i':
        print("interactive mode")
        return

    try:
        if args[0] == '-r':
            query_str = args[1]
            print(f"List of hosts for query string '{query_str}': ")
            search_hosts(INPUTFILE, query_str)
            return
    except Exception:
        print(f"List of hosts: ")
        search_hosts(INPUTFILE)
        return

    try:
        if args[0] == "-w":
            ip_addr = args[1]
            hostname = args[2]
            update_host(INPUTFILE, ip_addr, hostname)
            print("A new host record has been saved")
            return
    except IndexError:
        print("Please provide the IP and the hostname '-w 172.1.2.5 example.com'")
        return
    except InvalidIP as err:
        print(err)
        return
    except InvalidHostname as err:
        print(err)
        return


if __name__ == '__main__':
    main()
