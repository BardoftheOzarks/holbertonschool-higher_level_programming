#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for num in line:
            if num + 1 in line:
                print('{:d}'.format(num), end=' ')
            else:
                print('{:d}'.format(num))
    if matrix == [[]]:
        print()
