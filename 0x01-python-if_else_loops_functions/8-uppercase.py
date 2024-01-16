#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 97 and ord(str) <= 122:
        print("{}".format(chr(ord(str) - 32)))
    else:
        print("{}".format(str))

