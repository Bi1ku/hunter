def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


print(max(1, 2, 3))
print(max(4, 10, 8))
print(max(3, 8, 10))


def sum(arr):
    total = 0
    for num in arr:
        total += num

    return total


print(sum([1, 2, 3, 4, 5]))
print(sum([7, 3, 6, 78, 12, 3]))
print(sum([1198, 2, 12, 4, 5]))


def reverse(string):
    result = ""

    for i in range(len(string) - 1, -1, -1):
        result += string[i]

    return result


print(reverse("Hello, World!"))
