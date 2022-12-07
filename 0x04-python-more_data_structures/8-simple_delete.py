#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in list(a_dictionary):
        if k == key:
            del a_dictionary[key]
    return a_dictionary
