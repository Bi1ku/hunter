# Name: Owen Shi
# Date: Sept. 14th, 2024
# This program converts images to green scale

import matplotlib.pyplot as plt
import numpy as np

input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

img = plt.imread(input_file)  # Read in image from csBridge.png
plt.imshow(img)  # Load image into pyplot
plt.show()  # Show the image (waits until closed to continue)

img2 = img.copy()  # make a copy of our image
img2[:, :, 0] = 0  # Set the green channel to 0
img2[:, :, 2] = 0  # Set the blue channel to 0

plt.imshow(img2)  # Load our new image into pyplot
plt.show()  # Show the image (waits until closed to continue)

# Save the image we created to the file: reds.png
plt.imsave(output_file, img2)
