#!/usr/bin/python3
"""LockedClass"""


class LockedClass:
    """No class/object attribute.
    Prevent the user from dynamically creating new instance attributes.
    Except if it is called first_name.
    """
    __slots__ = ["first_name"]
