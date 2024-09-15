# Name: Owen Shi
# Date: Sept. 14th, 2024
# This program reverses an inputted message

message = input("Enter a message: ")

for x in range(len(message) - 1, -1, -1):
    print(message[x])
