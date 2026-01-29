#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        queens = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if queens < 4:
        print("N must be at least 4")
        exit(1)
