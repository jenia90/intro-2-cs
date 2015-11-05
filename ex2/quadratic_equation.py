#####################################################################
# FILE : quadratic_equation.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex2 2015-2016
# DESCRIPTION: Calculates the value of given quadratic equation.
#####################################################################

import math  # Imports the math module.


def quadratic_equation(a, b, c):
    """
    Calculates the equation with given coefficient values.
    """
    x1 = 0
    x2 = 0

    det = b**2 - 4*a*c

    if det < 0:  # Checks if the determinant equals to 0. If 'yes' returns None in both solutions.
        return None, None

    x1 = (-b + math.sqrt(det)) / 2*a  # Calculates the value of the first solution.
    x2 = (-b - math.sqrt(det)) / 2*a  # Calculates the value of the second solution.

    if x1 == x2:
        return x1, None
    else:
        return x1, x2


def quadratic_equation_user_input():
    """
    Asks the user to input coefficients and then prints the solution(s) of the equation.
    """
    values = input("Insert coefficients a,b, and c: ").split()  # Grabs input from the user and splits it into values
    ret1, ret2 = quadratic_equation(float(values[0]),
                                    float(values[1]),
                                    float(values[2]))  # Assigns the returned values to the variables.

    if ret2 is not None:  # Checks if the second value is empty.
        print("The equation has 2 solutions: " + str(ret1) + " and " + str(ret2))
    elif ret1 is None and ret2 is None:  # Checks if both values are empty.
        print("The equation has no solutions.")
    else:
        print("The equation has 1 solution: " + str(ret1))

