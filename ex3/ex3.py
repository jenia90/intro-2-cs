#####################################################################
# FILE : quadratic_equation.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex2 2015-2016
# DESCRIPTION: Calculates the value of given quadratic equation.
#####################################################################

import operator

def create_list():
    str_input = []
    while True:
        usr_input = input()

        if usr_input == "":
            return str_input
        else:
            str_input.append(usr_input)


def concat_list(lst_str):
    ret_str = ""
    for i in lst_str:
        ret_str += i

    return ret_str


def avr(num_list):
    avg = 0.0
    for n in num_list:
        avg += n

    return avg / len(num_list)


def cyclic(lst1, lst2):
    if len(lst1) != len(lst2):
        return None
    elif lst1 == lst2:
        return True

    for i in range(len(lst1)):
        if lst2 == list_shift(lst1, i):
            return True
        else:
            continue

    return False


def list_shift(lst, steps):
    new_lst = lst
    for i in range(len(lst)):
        new_lst[i] = lst[(i + int(steps)) % len(lst)]

    return new_lst


print(cyclic([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]))
