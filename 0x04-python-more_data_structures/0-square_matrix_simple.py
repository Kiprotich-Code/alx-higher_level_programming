#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_list = []
    for i in matrix:
        my_list.append(list(map(lambda i: i**2, i)))
    return my_list
