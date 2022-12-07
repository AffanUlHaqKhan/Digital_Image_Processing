import numpy
import cv2
import os
import math

os.chdir("F:\Sem Course\Sem6\DIP\LAB 2")
my_img=cv2.imread("Capture.png",0)

a = input("enter the downsampling amount: ")
a = int(a)

my_img1 = cv2.resize(my_img, (512,512))
r,c = numpy.shape(my_img1)
r1 = math.floor(r/a)
c1 = math.floor(c/a)
my_img2 = numpy.ones((r1,c1),dtype=numpy.uint8)

for i in range(0,r1,a):
    for j in range(0,c1,a):
        my_img2[i][j] = my_img1[i*a][j*a]


cv2.imshow("a",my_img2)
