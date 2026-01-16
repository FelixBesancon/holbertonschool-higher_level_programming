#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        label = "arguments."
    elif argc == 1:
        label = "argument:"
    else:
        label = "arguments:"
    print("{} {}".format(argc, label))
    for index in range(1, argc + 1):
        print("{}: {}".format(index, sys.argv[index]))
