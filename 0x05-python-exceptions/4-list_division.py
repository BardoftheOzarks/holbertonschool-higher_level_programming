#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for ele in range(list_length):
        try:
            new_ele = my_list_1[ele] / my_list_2[ele]
        except ZeroDivisionError:
            print('division by 0')
            new_ele = 0
        except TypeError:
            print('wrong type')
            new_ele = 0
        except IndexError:
            print('out of range')
            new_ele = 0
        finally:
            result.append(new_ele)
    return result
