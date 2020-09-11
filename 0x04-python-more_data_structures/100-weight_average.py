#!/usr/bin/python3
def mul(a, b):
    return a*b
def weight_average(my_list=[]):
    if my_list:
        for duple in my_list:
            score += duple[0] * duple[1]
            weight += duple[1]
        return score/weight
    else:
        return 0
