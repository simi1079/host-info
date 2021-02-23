import sys
from .lib import usage

INPUTFILE = "./hostsfile.txt"


def main():
    args = sys.argv[1:]

    if len(args) == 0 or args[0] == '-h' or args[0] == 'help':
        usage()
        return

    if args[0] == '-i':
        print("interactive mode")
        return


if __name__ == '__main__':
    main()
