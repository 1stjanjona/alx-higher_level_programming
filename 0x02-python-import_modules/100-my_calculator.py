#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculaotr.py <a> <opperator> <b>")
        sys.exit(1)
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]
    if operator not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, b = int(a), int(b)
    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        if b != 0:
            result = div(a, b)
    print("{:d} {} {:d} = {}".format(a, operator, b, result))
