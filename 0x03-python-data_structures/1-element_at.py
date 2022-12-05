#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > list_len:
        return None
    else:
        return my_list[idx]
