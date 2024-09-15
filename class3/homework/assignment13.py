# Name: Owen Shi
# Date: Sept. 14th, 2024
# This program turns hexcode into turtle color

import turtle

turtle.colormode(255)
t = turtle.Turtle()
t.shape("turtle")

hex = input("Enter a hex string: ")
r, g, b = "", "", ""

hex_map = "0123456789ABCDEF"


def convert_hex(code):
    num = 0
    for i in range(len(code) - 1, -1, -1):
        num += hex_map.find(code[i]) * 16 ** ((len(code) - 1) - i)
    return num


for i in range(1, len(hex)):
    if len(r) < 2:
        r += hex[i]
    elif len(g) < 2:
        g += hex[i]
    else:
        b += hex[i]


r, g, b = convert_hex(r), convert_hex(g), convert_hex(b)

t.color(r, g, b)
