#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for x in a_dictionary.keys():
        new_dict[x] *= 2
    return(new_dict)
