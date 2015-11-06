#####################################################################
# FILE : quadratic_equation.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex2 2015-2016
# DESCRIPTION: Calculates the value of given quadratic equation.
#####################################################################


def create_list():
    str_input = []
    while True:
        str_element = input()

        if str_element == "":
            return str_input
        else:
            str_input.append(str_element)


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
    for i in range(len(lst1)):
        if lst2 == (lst1[i:] + lst1[:i]) or lst2 == lst1:
            return True
        else:
            continue

    return False


def hist(list_num, n):
    ret_lst = [0] * n

    for i in range(n):
        for l in list_num:
            if l == i:
                ret_lst[i] += 1

    return ret_lst


def fact(n):
     # TODO: finish function implementation


print(fact(1))

# print(hist([3,5, 1,2,4,5,6,1,4,5,2,4], 6))
# print(cyclic(['a', 'b', 'c'], ['c', 'a', 'c']))
