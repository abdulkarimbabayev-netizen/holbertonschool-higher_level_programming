#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)
    result = 0
    for n in unique:
        result += n
    return result
