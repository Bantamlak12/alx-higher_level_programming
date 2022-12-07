#!/usr/bin/python3
def best_score(a_dictionary):
    return (max(set(a_dictionary)) if a_dictionary else None)
