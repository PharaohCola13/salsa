import matplotlib.pyplot as plt
from numpy import *
from skimage import io
from skimage.color import rgb2gray
from skimage.exposure import rescale_intensity
import datetime

print(datetime.datetime.now())

img = io.imread('./data/latest.jpg')

grayscale = rgb2gray(img)
final = rescale_intensity(grayscale, in_range=(0.3, 1))

plt.figure(0)
plt.imshow(grayscale, cmap=plt.cm.gray)
plt.axis('off')

plt.figure(1)
plt.imshow(final, cmap=plt.cm.gray)
plt.axis('off')
plt.show()
