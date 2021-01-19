#!/usr/bin/python3
def uppercase(str):
    for word in str:
        if 97 <= ord(word) <= 122:
            print(chr(ord(word) - 32), end='')
        else:
            print(word, end='')
