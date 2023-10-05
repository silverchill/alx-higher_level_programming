#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{0:d} arguments.".format(len(argv) - 1))
    elif len(argv) == 2:
        print("{0:d} argument:".format(len(argv) - 1))
        for w in range(len(argv) - 1):
            print("{0:d}: {1}".format(w + 1, argv[w + 1]))
    elif len(argv) > 2:
        print("{0:d} arguments:".format(len(argv) - 1))
        for w in range(len(argv) - 1):
            print("{0:d}: {1}".format(w + 1, argv[w + 1]))
