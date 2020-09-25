#!/usr/bin/python3
'''Divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''divides every element of each list in a matrix by div'''
    matrix_err = 'matrix must be a matrix (list of lists) of integers/float'
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) is not list:
        raise TypeError(matrix_err)
    size = len(matrix[0])
    for line in matrix:
        if type(line) is not list:
            raise TypeError(matrix_err)
        if len(line) is not size:
            raise TypeError('Each row of the matrix must have the same size')
        for num in line:
            if type(num) is not int and type(num) is not float:
                raise TypeError(matrix_err)
    return list(map(lambda line:
                    list(map(lambda x: round(x/div, 2), line)), matrix))
