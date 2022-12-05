#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    else:
        return (len(sentence), sentence[0])
