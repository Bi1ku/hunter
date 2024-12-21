# Name: Owen Shi
# Date: Fri., Nov. 1, 2024
# Assignment 34

import pandas as pd
import matplotlib.pyplot as plt

input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

homeless = pd.read_csv(input_file)

homeless["Fraction Children"] = (
    homeless["Total Children in Shelter"] / homeless["Total Individuals in Shelter"]
)

homeless.plot(x="Date of Census", y="Fraction Children")

plt.show()

fig = plt.gcf()
fig.savefig(output_file)
