# Name: Owen Shi
# Date: Sept. 13th, 2024
# This program returns a cesar cipher of a given message

message = input("Enter a word: ")

print("Your word in code is: ")

for letter in message:
    ciphered_letter = ""
    if ord(letter) + 13 > 122:
        ciphered_letter = chr((ord(letter) + 13) % 122 + ord("a") - 1)
    else:
        ciphered_letter = chr(ord(letter) + 13)

    print(ciphered_letter, end="")
