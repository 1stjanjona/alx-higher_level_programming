#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    elements = len(sys.argv) - 1
    if elements == 0:
        print("0 arguments.")
    elif elements == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(elements))
    for ndx in range(elements):
        print("{:d}: {}".format(ndx + 1, sys.argv[ndx + 1]))
