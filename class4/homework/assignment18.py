# Name: Owen Shi
# Date: Oct 4th, 2024
# Assignment 18

import turtle

t = turtle.Turtle()

angles = []

for i in range(5):
    angles.append(int(input("Enter a number: ")))

for angle in angles:
    t.left(angle)
    t.forward(100)
