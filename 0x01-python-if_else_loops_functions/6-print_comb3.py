#!/usr/bin/python3
for frst in range(10):
    for scnd in range(frst, 10):
        if frst < scnd:
            if frst == 8 and scnd == 9:
                print("{:d}{:d}".format(frst, scnd), end="\n")
            else:
                print("{:d}{:d}".format(frst, scnd), end=", ")
