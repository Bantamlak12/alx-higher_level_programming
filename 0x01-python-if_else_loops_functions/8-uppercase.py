#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        if ord(char) in range(97, 123):
            upper += chr(ord(char) - 32)
        elif ord(char) in range(65, 91):
            upper += chr(ord(char))
        elif ord(char) in range(48, 58):
            upper += chr(ord(char))
        elif ord(char) == 32:
            upper += chr(ord(char))
    print("{}".format(upper))
