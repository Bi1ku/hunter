# Name: Owen Shi
# Date: Sept. 14th, 2024
# This program turns hexcode into turtle color

import turtle

turtle.colormode(255)
t = turtle.Turtle()
t.shape("turtle")

hex = input("Enter a hex string: ")

t.color(hex)
