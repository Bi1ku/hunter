# Name: Owen Shi
# Sunday, Oct. 27th, 2024
# Assignment 28

import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv("nycHistPop.csv", skiprows=5)

borough = input("Enter borough name: ")
output_name = input("Enter the output file name: ")

csv["Fraction"] = csv[borough] / csv["Total"]
csv.plot(x="Year", y="Fraction")

figure = plt.gcf()
figure.savefig(output_name)
