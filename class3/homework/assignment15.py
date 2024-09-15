# Name: Owen Shi
# Date: Sept. 14th, 2024
# This program converts binary to decimal

binary = input("Enter binary number: ")

sum = 0
for i in range(len(binary) - 1, -1, -1):
    sum += int(binary[i]) * 2 ** ((len(binary) - 1) - i)

print("Your number in decimal is", sum)
