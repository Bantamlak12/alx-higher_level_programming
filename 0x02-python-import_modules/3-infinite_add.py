#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args == 0:
        print(args)
    else:
        result = 0
        for number in range(1, len(sys.argv)):
            result += int(sys.argv[number])
        print(result)
