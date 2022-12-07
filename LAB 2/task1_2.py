import numpy
import cv2
import os

os.chdir("F:\DIP")
my_img=cv2.imread("Capture.png",0)

r,c=numpy.shape(my_img)
my_array = numpy.ones((r,c))

for i in range(r):
    for j in range(c):
        my_array[i][j]= my_img[-i][j]

cv2.imshow("a",my_img)

for i in range(r):
    for j in range(c):
        my_img[i][j] = my_array[i][j]


cv2.imshow("b",my_img)
