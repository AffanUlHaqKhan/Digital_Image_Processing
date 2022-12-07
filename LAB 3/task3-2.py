import numpy
import cv2
import os
import math

img = numpy.ones((501,501),dtype=numpy.uint8)
img = 255*img

for i in range(0,501):
    for j in range(0,501):
        img[i][j] = math.sqrt((i-251)**2+(j-251)**2)

cv2.imshow("test",img)
