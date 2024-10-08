# Name: Owen Shi
# Date: Sept. 4th, 2023
# This program is for assignment 5

import turtle

wn = turtle.Screen()  # Set up the window and its attributes
wn.bgcolor("purple")


tess = turtle.Turtle()  # create tess and set some attributes
tess.color("white")
tess.pensize(5)

alex = turtle.Turtle()  # create alex

tess.forward(80)  # Let tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)  # complete the triangle

tess.right(180)  # turn tess around
tess.forward(80)  # move her away from the origin

alex.forward(50)  # make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.exitonclick()
