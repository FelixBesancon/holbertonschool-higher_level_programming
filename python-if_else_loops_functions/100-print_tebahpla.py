#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(letter - 32) if letter % 2 else chr(letter)), end="")
