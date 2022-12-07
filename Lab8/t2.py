import numpy
import cv2
import math
import os

my_img = cv2.imread("Fig01.tif",0)
my_img = numpy.double(my_img)
r,c = numpy.shape(my_img)

lp_img = numpy.zeros((r,c),dtype = numpy.double)
hp_img = numpy.zeros((r,c),dtype = numpy.double)
dm_img = numpy.zeros((r,c),dtype = numpy.double)
f_img = numpy.zeros((r,c),dtype = numpy.double)
if_img = numpy.zeros((r,c),dtype = numpy.double)
rif_img = numpy.zeros((r,c),dtype = numpy.double)
rf_img = numpy.zeros((r,c),dtype = numpy.double)

rm = int(r/2)
cm = int(c/2)
sigma = 30

for i in range(r):
    for j in range(c):
        temp = numpy.sqrt(numpy.square(rm-i)+numpy.square(cm-j))
        dm_img[i][j] = temp
cv2.imshow("DM",dm_img/255)

for i in range(r):
    for j in range(c):
        lp_img[i][j] = numpy.exp((-1*(dm_img[i][j]**2))/(2*(sigma**2)))
cv2.imshow("LP",lp_img)

maxl = numpy.max(lp_img)
for i in range(r):
    for j in range(c):
       hp_img[i][j] = maxl - lp_img[i][j]
cv2.imshow("HP",hp_img)

f_img = numpy.fft.fft2(my_img)
f_img = numpy.fft.fftshift(f_img)
rf_img = f_img * lp_img
rf_img = numpy.fft.ifftshift(rf_img)
rf_img = numpy.fft.ifft2(rf_img)
rf_img = numpy.absolute(rf_img)

if_img = numpy.fft.fft2(my_img)
if_img = numpy.fft.fftshift(if_img)
rif_img = if_img * hp_img
rif_img = numpy.fft.ifftshift(rif_img)
rif_img = numpy.fft.ifft2(rif_img)
rif_img = numpy.absolute(rif_img)

mini = numpy.min(rf_img)
maxi = numpy.max(rf_img)
mini1 = numpy.min(rif_img)
maxi1 = numpy.max(rif_img)

for i in range(r):
    for j in range(c):
        rf_img[i][j] = ((rf_img[i][j]-mini)*255)/(maxi-mini)
        rif_img[i][j] = ((rif_img[i][j]-mini1)*255)/(maxi1-mini1)
rf_img = numpy.uint8(rf_img)
rif_img = numpy.uint8(rif_img)
cv2.imshow("RESULT",rf_img)
cv2.imshow("RESULT1",rif_img)


