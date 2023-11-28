#!/usr/bin/python3
"""text_indentation"""


def text_identification(text):
    """Add 2 lines after each of ., ?, :
    Args:
        text: string text
    Raises:
        TypeError: if text not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for chrs in '.?:':
        for line in text.split(chrs):
            text = (chrs + "\n\n").join(line.strip(" "))
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
