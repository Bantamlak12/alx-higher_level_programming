#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list) - 1
    list_orig = my_list.copy()
    list_copy = my_list.copy()
    list_copy[idx] = element
    if idx < 0:
        return list_orig
    elif idx > list_len:
        return list_orig
    else:
        return list_copy
