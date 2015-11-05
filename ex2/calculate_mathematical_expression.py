#####################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex2 2015-2016
# DESCRIPTION: A program to perform a math operation on
#               2 given numbers.
#####################################################################


def calculate_mathematical_expression(num1, num2, sign):
    """
    Calculates the value of an expression for the 2 given numbers and the operation.
    """
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "/":
        if num2 == 0:
            return None
        return num1 / num2
    else:
        return None


def calculate_from_string(expr):
    """
    Splits the string expression into 2 numbers and the operation
    and passes it to the calculate_mathematical_expression function.
    """
    val_array = expr.split()
    return calculate_mathematical_expression(float(val_array[0]),
                                             float(val_array[2]),
                                             val_array[1])

