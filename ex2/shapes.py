#####################################################################
# FILE : shapes.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex2 2015-2016
# DESCRIPTION: A program to calculate the area of different shapes.
#####################################################################

import math


def shape_area():
    """
    Prints a multi-choice menu and calls the corresponding function.
    """
    shape = int(input("Choose shape (1=circle, 2=rectangle, 3=trapezoid): "))

    if shape < 1 or shape > 3:
        return None  # In case of invalid input returns None

    elif shape == 1:
        return circle_area(input())  # Returns the value of circle area calculation.

    elif shape == 2:
        return rectangle_area(input(), input())  # Returns the value of rectangle area calculation.

    else:
        return trapezoid_area(input(), input(), input())  # Returns the value of trapezoid area calculation.


def trapezoid_area(a, b, h):
    """
    Calculates the area of a trapezoid with given measurements.
    """
    return ((float(a) + float(b)) * float(h)) / 2


def rectangle_area(a, b):
    """
    Calculates the area of a rectangle with given sides.
    """
    return float(a) * float(b)


def circle_area(r):
    """
    Calculates the area of a circle with given radius.
    """
    return (float(r) ** 2) * math.pi
