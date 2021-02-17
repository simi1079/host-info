import sys
from .lib import usage


def main():
    args = sys.argv[1:]

    if args[0] == '-i':
        return

    if args[0] == '-h' or args[0] == 'help':
        usage()


if __name__ == '__main__':
    main()
