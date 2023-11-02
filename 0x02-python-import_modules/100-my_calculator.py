#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculaotr.py <a> <opperator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operator: +, -, *, /")
        exit(1)
