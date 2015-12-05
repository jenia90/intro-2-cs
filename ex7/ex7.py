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
    if n > 0:
        print_to_n(n-1)
        print(n)


def print_reversed_n(n):
    """
    prints all the numbers from n to 1
    :param n: the first number to print
    """
    if n > 0:
        print(n)
        print_reversed_n(n-1)


def has_divisor_smaller_than(n, i):
    """
    checks if the number has smaller divisor than the second parameter
    :param n: the number to check
    :param i: divisor candidate
    :return: False if no divisors and True if there are any
    """
    if i == 1:
        return False
    elif n % i == 0 and i != 1:
        return True
    else:
        return has_divisor_smaller_than(n, i-1)


def is_prime(n):
    """
    checks if the given number is a prime
    :param n: number to check
    :return: True if prime and False if not
    """
    return False if n == 1 or has_divisor_smaller_than(n, n-1) else True


def list_divisors(n, divs, d=2):
    """
    helper function for the divisors function to create a list of divisors
    :param n: original number to process
    :param divs: list of divisors
    :param d: (optional) the divisor to check
    :return: returns a list of divisors
    """
    # checks if the current divisor is smaller than original number
    if n > d:
        if n % d == 0:  # checks if current divisor candidate is correct
            divs.append(d)  # if yes appends it to the list

        # recursive call to find next divisor
        return list_divisors(n, divs, d+1)
    # condition for when the number is the divisor of itself
    elif n not in divs:
        divs.append(n)

    return divs


def divisors(n):
    """
    Creates a list of divisors of a given number
    :param n: number to process
    :return: returns a list of divisors
    """
    # returns empty list in case the number is 0
    if n == 0:
        return []

    return list_divisors(abs(n), [1])


def factorial(n):
    """
    helper function to find the factorial of a given number
    :param n: the number to process
    :return: returns n!
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def exp_helper(n, x, i=0):
    """
    helper function for the exp_n_x
    :param i: the counter of the sum going from 0 to n
    :param x: the power of e
    :param n: the number
    """
    if n == i:
        return (x**i)/factorial(i)
    return exp_helper(n, x, i+1) + (x**i)/factorial(i)


def exp_n_x(n ,x):
    """
    finds the exponent of a number
    :param n: the number itself
    :param x: the power of e
    :return: returns the exponent
    """
    return exp_helper(n, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    implementation of the hanoi tower game where the computer is expected to
    move disks from one tower to the other using a temporary tower.
    :param hanoi: hanoi game object
    :param n: number of disks
    :param src: source tower (game object)
    :param dest: destination tower (game object)
    :param temp: temporary tower (game object)
    """
    if n > 0:
        # recursive call to move n-1 disks to the temp tower using dest tower
        play_hanoi(hanoi, n-1, src, temp, dest)

        # instruction to move disks
        hanoi.move(src, dest)

        # recursive call to move n-1 disks to the dest tower using src tower
        play_hanoi(hanoi, n-1, temp, dest, src)


def print_binary_sequences_with_prefix(prefix, n):
    pass


def print_binary_sequences(n):
    pass