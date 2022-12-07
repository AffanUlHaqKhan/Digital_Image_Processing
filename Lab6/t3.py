import numpy
import cv2
import os
import math


my_img = cv2.imread("Fig03.tif",0)
r,c = numpy.shape(my_img)
my_img = numpy.double(my_img)
my_img1 = numpy.ones((r,c),dtype=numpy.double)


lp = numpy.ones((3,3),dtype = numpy.double)
lp[0][0]= -1
lp[0][1]= -1
lp[0][2]= -1
lp[1][0]= -1
lp[1][1]= 8
lp[1][2]= -1
lp[2][0]= -1
lp[2][1]= -1
lp[2][2]= -1

print(lp)

lp_img = numpy.ones((r,c),dtype = numpy.double)
lp_img = cv2.filter2D(my_img,-1, lp)
add_img = numpy.zeros((r,c),numpy.double)
add_img = my_img+lp_img

r1,c1 = numpy.shape(lp_img)

maximum = 0
minimum = 255
for i in range(r1):
    for j in range(c1):
        if add_img[i][j] < minimum:
            minimum = add_img[i][j]
        if add_img[i][j] > maximum:
            maximum = add_img[i][j]
print(maximum)
print(minimum)
for i in range(r1):
    for j in range(c1):
        my_img1[i][j] = ((add_img[i][j]-minimum)*255/(maximum-minimum))
my_img1 = numpy.uint8(my_img1)
cv2.imshow("a",my_img1)

