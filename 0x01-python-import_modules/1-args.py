#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for x, arg in enumerate(argv, start=1):
        print("{}: {}".format(x, arg))

if __name__ == "__main__":
    main()
