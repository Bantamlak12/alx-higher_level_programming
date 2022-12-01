#!/usr/bin/python3
import sys
args = len(sys.argv) - 1
if args == 0:
    print(args, "arguments.")
elif args == 1:
    print(args, "argument:")
    print("{}: {}".format(args, sys.argv[1]))
else:
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
