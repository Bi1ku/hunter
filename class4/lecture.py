import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("csBridge.png")
plt.imshow(img)
plt.show()

img2 = img.copy()
img2[:, :, 1] = 0

plt.imshow(img2)
plt.show()

plt.imsave("reds.png", img2)
