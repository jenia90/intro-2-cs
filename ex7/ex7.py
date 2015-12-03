##################################################
#  FILE: ex7.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex7 2015-2016
#  DESCRIPTION : 
#
##################################################


def print_to_n(n):
    """
    prints all the numbers from 1 to n
    :param n: last number to print
    """
    if n == 1:
        print(n)
    else:
        print_to_n(n - 1)
        print(n)


def print_reversed(n):
    """
    prints all the numbers from n to 1
    :param n: the first number to print
    """
    if n != 1:
        print(n)
        print_reversed(n-1)
    else:
        print(n)


def is_prime(n):
    pass


print_to_n(10)