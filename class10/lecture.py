import turtle


def max(a, b):
    if a > b:
        return a
    return b


def three_max(a, b, c):
    return max(max(a, b), c)


def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


def multiply(arr):
    product = 0
    for i in arr:
        product *= i
    return product


def reverse_str(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


def setUp():
    t = turtle.Turtle()
    t.color("purple")
    t.penup()
    return t


def getInput():
    x = int(input("X: "))
    y = int(input("Y: "))
    return (x, y)


def maxLocation(t, x, y):
    t.goto(x, y)
    t.stamp()


def main():
    tess = setUp()
    for i in range(5):
        x, y = getInput()
        maxLocation(tess, x, y)
