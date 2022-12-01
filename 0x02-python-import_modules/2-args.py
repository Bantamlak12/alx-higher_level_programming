#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 0:
        print(args, "arguments.")
    elif args == 1:
        print(args, "argument:")
        print("{}: {}".format(args, sys.argv[1]))
    else:
        print(len(sys.argv) - 1, "arguments:")
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
