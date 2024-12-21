# Name: Owen Shi
# Date: Fri. Nov. 8th, 2024
# Assignment 39

import pandas as pd

input_file = input("Enter CSV file name: ")

print("Top three contributing factors for collisions: ")

df = pd.read_csv(input_file)

print("Top three contributing factors for collisions:")
print(df["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
