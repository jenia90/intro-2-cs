#####################################################################
# FILE : ex3.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex3 2015-2016
# DESCRIPTION: Exercise containing few functions to practice loops,
#               lists and variables
#####################################################################


def create_list():
    """
    Creates a list from separate user inputs. Quits on blank input
    :return: Returns a list of strings from user input
    """
    str_input = []
    while True:
        str_element = input()  # Grabs input from the user

        if str_element == "":  # Checks if the input is an empty string
            return str_input  # if yes, returns the list of strings
        else:
            str_input.append(str_element)


def concat_list(lst_str):
    """
    Concatenates the strings in the lst_str variables into one string
    :param lst_str: List of strings to concatenate
    :return: Concatenated string
    """
    new_str = ""
    for i in lst_str:  # the loop goes through all the strings and connects them
        new_str += i

    return new_str


def avr(num_list):
    """
    Calculates the average of a list of numbers
    :param num_list: List of numbers to average
    :return: The average of given numbers
    """
    avg = 0.0
    for n in num_list:
        avg += n

    return avg / len(num_list)


def cyclic(lst1, lst2):
    """
    Checks if the first list is cyclic shift of the second list
    :param lst1: First list
    :param lst2: Second List
    :return: Returns True if yes otherwise returns False
    """
    for i in range(len(lst1)):
        if lst2 == (lst1[i:] + lst1[:i]) or lst2 == lst1:
            return True  # Slices the first string at 'i' position and connects to the end, rotating it 'i' steps
        else:
            continue

    return False


def hist(n, num_list):
    """
    Histogram of a given list.
    :param n: The range of numbers to check
    :param num_list: List of numbers to check
    :return: Returns the amount of times each number in range appeared in the list
    """
    new_lst = [0] * n

    for i in range(n):
        for l in num_list:
            if l == i:
                new_lst[i] += 1  # If number from the range appears in the list, increment the value by 1

    return new_lst


def fact(n):
    """
    Calculates the factorization of a given number
    :param n: Number to factorize
    :return: Returns the factorization list
    """
    new_lst = []

    for i in range(2, n):  # Goes every number in range from 2 to n
        while n % i == 0:  # Checks if modulo of n and i equals to 0
            new_lst.append(i)  # Adds the i value to the list
            n /= i

    return new_lst


def cart(lst1, lst2):
    """
    Calculates the Cartesian product of 2 lists
    :param lst1: First list
    :param lst2: Second list
    :return: Returns a list of pairs in the Cartesian product
    """
    cart_prod = []

    for f in lst1:
        for s in lst2:
            cart_prod.append([f, s])  # Adds the pair to the list

    return cart_prod


def pair(n, num_list):
    """
    Given a number and a list of numbers returns pairs of number which when added equal to n.
    :param n: The number which will equal to the sums of pairs
    :param num_list: List of numbers to check
    :return: Returns pairs of numbers whose sums equal to n
    """
    pairs = []

    for i in num_list:
        for j in num_list[num_list.index(i)+1:]:  # starts the list at the next index after i to remove duplicates
            if i + j == n:  # Checks if the sum equals to n
                pairs.append([i, j])

    if len(pairs) == 0:  # Checks if list of pairs equals to 0 if yes, returns None
        return None

    return pairs
