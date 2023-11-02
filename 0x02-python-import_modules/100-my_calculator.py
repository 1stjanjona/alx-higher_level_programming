#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculaotr.py <a> <opperator> <b>")
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    if operator not in operators:
        print("Unknown operator. Available operator: +, -, * and /")
        exit(1)
    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
