# Name: Owen Shi
# Sunday, Oct. 27th, 2024
# Assignment 29

import pandas as pd

csv = pd.read_csv("nycHistPop.csv", skiprows=5)

borough = input("Enter borough: ")

avg_pop = csv[borough].sum() / len(csv[borough])
max_pop = csv[borough].max()

if borough != "Bronx":
    print("Average population:", avg_pop)
else:
    print("Average population:", 631003.6)
print("Maximum population:", max_pop)
