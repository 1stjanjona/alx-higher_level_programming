#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence[0] = None
    if sentence and len(sentence) > 0:
        return (len(sentence), sentence[0])
