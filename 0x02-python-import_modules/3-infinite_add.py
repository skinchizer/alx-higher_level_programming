#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1
    sums = 0
    for i in range(args):
        sums += int(sys.argv[i + 1])
    print("{}".format(sums))
