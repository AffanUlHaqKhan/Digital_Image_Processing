import os
import numpy
import cv2
import copy
import math

my_img = cv2.imread("Fig01.tif",0)
my_img1 = cv2.resize(my_img,(64,64))
r,c = numpy.shape(my_img1)

my_img = numpy.uint8(my_img)

new_img = copy.deepcopy(my_img)
res_img = copy.deepcopy(my_img)

new_img = numpy.fft.fft2(my_img)
new_img = abs(new_img)
new_img = numpy.fft.fftshift(new_img)
res_img = cv2.normalize(new_img,res_img,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)

res_img = numpy.uint8(res_img)
cv2.imshow("c",res_img)

t_img = numpy.zeros((r,c), dtype = numpy.double)

for i in range(r):
    for j in range(c):
        my_img1[i][j] = my_img1[i][j]*(-1)**(i+j)
cv2.imshow("a",my_img1)

for i in range(r):
    for j in range(c):
        su = 0
        for x in range(r):
            for y in range(c):
                su =  abs(numpy.real(su+my_img1[x][y]*numpy.exp(-1j*2*numpy.pi*
                                                           ((i*x/64)+(j*y/64)))))
        t_img[i][j] = su
t_img = cv2.normalize(t_img,t_img,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)
t_img = numpy.uint8(t_img)
cv2.imshow("b",t_img)


