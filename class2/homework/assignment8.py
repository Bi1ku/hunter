# Name: Owen Shi
# Date: Sept. 13th, 2024
# This program prints the ascii of a inputted string

message = input("Enter a phrase: ")
print("In ASCII:")

for letter in message:
    print(ord(letter))
