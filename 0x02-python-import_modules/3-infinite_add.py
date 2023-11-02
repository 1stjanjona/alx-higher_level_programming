#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    elements = len(sys.argv) - 1
    add_args = 0
    for ndx in range(elements):
        add_args += int(sys.argv[ndx + 1])
    print(add_args)
