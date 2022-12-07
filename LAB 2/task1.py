import numpy
import cv2
import os

os.chdir("D:\DIP")
my_img = cv2.imread("Capture.png",0)
x,y=numpy.shape(my_img)

for i in range(x):
    for j in range(y):
        my_img[-i][j]= my_img[i][j]

cv2.imshow("task1",my_img)
