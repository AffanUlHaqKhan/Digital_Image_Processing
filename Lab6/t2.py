
import numpy
import cv2
import os
import math


my_img = cv2.imread("Fig01.tif",0)
cv2.imshow("original",my_img)
r,c = numpy.shape(my_img)


hs = numpy.array(([-1,-2,-1],[0,0,0],[1,2,1]))
hs = numpy.double(hs)
print(hs)

vs = numpy.array(([-1,0,1],[-2,0,2],[-1,0,1]))
vs = numpy.double(vs)
print(vs)

hs_img = numpy.ones((r,c),dtype = numpy.double)
vs_img = numpy.ones((r,c),dtype = numpy.double)

hs_img = cv2.filter2D(my_img,-1,hs)
hs_img = numpy.uint8(hs_img)

vs_img = cv2.filter2D(my_img,-1,vs)
vs_img = numpy.uint8(vs_img)

add_img = numpy.zeros((r,c),numpy.uint8)
add_img = hs_img+vs_img

cv2.imshow("a",hs_img)
cv2.imshow("b",vs_img)
cv2.imshow("c",add_img)
