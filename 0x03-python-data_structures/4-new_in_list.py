#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_len = len(my_list) - 1
    list_copy = my_list.copy()
    list_copy[idx] = element
    if idx < 0:
        return my_list
    elif idx > list_len:
        return my_list
    else:
        return list_copy
