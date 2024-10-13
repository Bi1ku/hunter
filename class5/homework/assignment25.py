# Name: Owen Shi
# Oct. 13th, 2024
# Assignment 25

import turtle

t = turtle.Turtle()
myWin = turtle.Screen()

number = int(input("Enter a whole number: "))

if number % 2 == 0:
    t.color("blue")
    t.backward(100)
else:
    t.color("red")
    t.forward(150)

myWin.exitonclick()
