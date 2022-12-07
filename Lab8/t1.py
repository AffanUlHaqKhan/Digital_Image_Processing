import numpy
import cv2
import math
import os

my_img = cv2.imread("Fig01.tif",0)
my_img = numpy.double(my_img)
r,c = numpy.shape(my_img)

dm_img = numpy.zeros((r,c),dtype = numpy.double)
lp_img = numpy.zeros((r,c),dtype = numpy.double)
hp_img = numpy.zeros((r,c),dtype = numpy.double)
t_img = numpy.zeros((r,c), dtype = numpy.double)
r_img = numpy.zeros((r,c), dtype = numpy.double)

rm = int(r/2)
cm = int(c/2)

for i in range(r):
    for j in range(c):
        temp = numpy.sqrt(numpy.square(rm-i)+numpy.square(cm-j))
        dm_img[i][j] = temp
cv2.imshow("DM",dm_img/255)

for i in range(r):
    for j in range(c):
        if dm_img[i][j]>=100:
            lp_img[i][j]=0
        elif dm_img[i][j]<100:
            lp_img[i][j]=1
cv2.imshow("LP",lp_img)

for i in range(r):
    for j in range(c):
       hp_img[i][j] = 1 - lp_img[i][j]
cv2.imshow("HP",hp_img)

t_img = numpy.fft.fft2(my_img)
t_img = numpy.fft.fftshift(t_img)
r_img = t_img * hp_img
r_img = numpy.fft.ifftshift(r_img)
r_img = numpy.fft.ifft2(r_img)
r_img = numpy.absolute(r_img)

mini = numpy.min(r_img)
maxi = numpy.max(r_img)
for i in range(r):
    for j in range(c):
        r_img[i][j] = ((r_img[i][j]-mini)*255)/(maxi-mini)
r_img = numpy.uint8(r_img)
cv2.imshow("RESULT",r_img)
