#!/usr/bin/python3
''' 100-my_int.pyModule'''


class MyInt(int):
    '''Class MyInt inverted'''

    def __eq__(self, other):
        '''Equal is actyally not equal'''
        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal here is Equal"""
        return super().__eq__(other)
