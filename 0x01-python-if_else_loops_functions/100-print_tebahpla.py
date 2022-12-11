#!/usr/bin/python3
for i in reversed(range(97, 123)):
        print(chr(i) if i % 2 == 0 else chr(i - 32), end="")
