#!/usr/bin/python3
"""1-my_liSt.py Module"""


class MyList(list):
    ''''Inheritance of MyList'''

    def print_sorted(self):
        '''Print list of MyList in ascending sort.
        Assume all the list are integers
        '''
        print(sorted(self))
