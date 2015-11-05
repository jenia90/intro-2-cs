#####################################################################
# FILE : largest_and_smallest.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex2 2015-2016
# DESCRIPTION: A program that finds the smallest and largest
#               number out of 3 given numbers.
#####################################################################


def largest_and_smallest(num1, num2, num3):
    """
    Finds the largest and smallest number out of 3 given.
    """
    largest = 0
    smallest = 0
    if num1 <= num2:
        if num2 <= num3:
            largest = num3
            smallest = num1
        else:
            largest = num2
            if num1 <= num3:
                smallest = num1
            else:
                smallest = num3
    elif num1 > num2:
        if num3 <= num1:
            largest = num1
            if num3 <= num2:
                smallest = num3
            else:
                smallest = num2
        else:
            largest = num3
            smallest = num2

    return largest, smallest  # Returns the numbers.

