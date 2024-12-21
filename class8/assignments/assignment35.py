# Name: Owen Shi
# Date: Fri, Nov. 1st, 2024
# Assignment 35

import matplotlib.pyplot as plt

in_file = input("Enter image file name: ")
out_file = input("Enter output file: ")

img = plt.imread(in_file)

img = img[round(len(img) // 2) :, : round(len(img[0]) // 2)]

plt.imsave(out_file, img)
