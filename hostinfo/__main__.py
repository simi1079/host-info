import sys
from .lib import usage, search_hosts

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
    except Exception:
        print(f"List of hosts: ")
        search_hosts(INPUTFILE)


if __name__ == '__main__':
    main()
