#!/usr/bin/python3
for letter in range(ord("a"), ord("z")+1):
    if (letter == ord("q") or letter == ord("e")):
        continue
    print("{}".format(chr(letter)), end="")
