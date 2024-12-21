import matplotlib.pyplot as plt
import pandas as pd

img = plt.imread("hunter.png")

img = img[round(len(img) / 2) : len(img), 0 : round(len(img[0]) / 2)]
# can do img.shape[0] to get height and img.shape[1] to get width.
# can be simplified to [round(len(img) / 2):, round(len(img[0] / 2)):]
#
# plt.imsave("test.png", img)
#
# plt.imshow(img)
# plt.show()
