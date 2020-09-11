#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    weight = 0
    if my_list:
        for duple in my_list:
            score += duple[0] * duple[1]
            weight += duple[1]
        return score/weight
    else:
        return 0
