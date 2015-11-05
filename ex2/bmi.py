#####################################################################
# FILE : bmi.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex2 2015-2016
# DESCRIPTION: A program to based on passed spell/hour and wand length
#               decide if the wizard is intelligent enough.
#####################################################################


def is_normal_bmi(spells_per_hour, wand):
    """
    Checks is if the wizard is intelligent enough.
    """
    if wand == 0:  # Handles the event of wand = 0.
        return None

    bmi = spells_per_hour / (wand ** 2)  # Calculates the BMI.

    if 24.9 >= bmi > 18.5:
        return True

    else:
        return False

