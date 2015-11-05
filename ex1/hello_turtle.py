#####################################################################
# FILE : hello_turtle.py
# WRITER : yevgeni, jenia90, 32088421
# EXERCISE : intro2cs ex1 2015-2016
# DESCRIPTION: A simple program to practice function implementation
#####################################################################

import turtle


def draw_petal():
    # This function draws the petals of the flower by moving the turtles head.
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)


def draw_flower():
    # This function draws a flower by using the draw_petal function and adds the rest.
    turtle.right(45)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(135)
    turtle.forward(150)


def draw_flower_advanced():
    # This function draws a flower using draw_flower function and moves the turtle away
    draw_flower()
    turtle.left(90)
    turtle.up()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()


def draw_flower_bed():
    # This function draws multiple flowers using the draw_flower_advanced function
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()
    turtle.done()

draw_flower_bed()
