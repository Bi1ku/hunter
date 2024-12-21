# Name: Owen Shi
# Date: Fri, Nov 8, 2024
# Assignment 36

import pandas as pd

input_file = input("Enter file name: ")
attribute = input("Enter attribute: ")

df = pd.read_csv(input_file)

print("The 10 worst offenders are: ")
print(df[attribute].value_counts()[:10])
