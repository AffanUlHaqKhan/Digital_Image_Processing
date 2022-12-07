import os
import numpy
import cv2
import math

my_img = cv2.imread("Fig01.tif",0)
my_img = numpy.double(my_img)
r,c = numpy.shape(my_img)
my_img1 = numpy.zeros((r,c),dtype=numpy.double)

cx = int(r/2)
cy = int(c/2)

for i in range(r):
    for j in range(c):
        value = numpy.sqrt(numpy.square(cx - i) + numpy.square(cy - j))
        if value > 255:
            value = 255
        my_img1[i][j] = value
cv2.imshow("dist",my_img1)

for i in range(r):
    for j in range(c):
        if my_img1[i][j]>=40:
            my_img1[i][j]=255
        elif my_img1[i][j]<40:
            my_img1[i][j]=0
cv2.imshow("thresh",my_img1)

t_img = numpy.fft.fft2(my_img)
t_img = numpy.fft.fftshift(t_img)
res_img = t_img * my_img

res_img=numpy.fft.ifftshift(res_img)
res_img = numpy.fft.ifft2(res_img)

mi = numpy.min(res_img);
ma = numpy.max(res_img);
r1,c1 = numpy.shape(res_img)
    
for i in range(r):
    for j in range(c):
        res_img[i][j] = ((res_img[i][j]- mi)/ (ma - mi)) * 255;

res_img = numpy.uint8(res_img)

cv2.imshow("Result",res_img)
