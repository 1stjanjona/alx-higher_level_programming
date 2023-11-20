
#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    ntgr = True
    try:
        print("{:d}".format(value))
    except Exception as exp:
        print("Exception:", exp, file=sys.stderr)
        ntgr = False
    return ntgr
