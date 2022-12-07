#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        return (a_dictionary.update({key: value}))
    else:
        return None
