import numpy
import os
import cv2
import math

my_img = cv2.imread("fig01.tif",0)
arr = numpy.shape(my_img)
my_img1 = numpy.ones((arr[0],arr[1]), dtype = numpy.uint8)
my_img2 = numpy.ones((arr[0],arr[1]), dtype = numpy.uint8)
mean = 200
print(mean)

for i in range(arr[0]):
    for j in range(arr[1]):
        if my_img[i][j] < mean:
            my_img1[i][j]=0
        elif my_img[i][j] > mean:
            my_img1[i][j]=255

cv2.imshow("Binary",my_img1)

for i in range(arr[0]):
    for j in range(arr[1]):
        temp = (256-1)-my_img[i][j]
        my_img2[i][j]=temp

cv2.imshow("Negative",my_img2)
cv2.imwrite("a1.tif",my_img1)
