# Name: Owen Shi
# Date: Fri, Nov. 1st, 2024
# Assignment 33

nouns = input("Enter nouns: ")

count = 0
words = nouns.split(" ")

for noun in words:
    if noun[-1] == "s":
        count += 1

print("Number of words:", len(words))
print("Fraction of your list that is plural is", count / len(words))
