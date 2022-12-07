import numpy
import cv2
import math
import os

my_img = cv2.imread("Fig01.tif",0)
my_img = numpy.double(my_img)
r,c = numpy.shape(my_img)
print(r,c)
fil = numpy.zeros((9,9),dtype = numpy.double)
r1 = r+9-1
c1 = c+9-1

pad_img = numpy.zeros((r1,c1),dtype = numpy.double)
pad_fil = numpy.zeros((r1,c1),dtype = numpy.double)
t_img = numpy.zeros((r1,c1),dtype = numpy.double)
t_fil = numpy.zeros((r1,c1),dtype = numpy.double)
r_img = numpy.zeros((r1,c1),dtype = numpy.double)


for i in range(9):
    for j in range(9):
        if(i == 0 or i == 8 or j == 0 or j == 8):
            fil[i][j] = 1;
        elif(i==1 or i == 7 or j ==1 or j==7):
            fil[i][j] = 2;
        elif(i== 2 or i == 6 or j ==2 or j ==6):
            fil[i][j] = 4;
        elif(i== 3 or i ==5  or j ==3 or j ==5):
            fil[i][j] = 8;
        else:
            fil[4][4] = 16;

for i in range(r1):
    for j in range(c1):
        if i < r and j < c:
            pad_img[i][j] = my_img[i][j]
        else:
            pad_img[i][j] = 0
cv2.imshow("Pad_IMG",pad_img)

for i in range(r1):
    for j in range(c1):
        if i < 9 and j < 9:
            pad_fil[i][j] = fil[i][j]
        else:
            pad_fil[i][j] = 0
cv2.imshow("Pad_Filter",pad_fil)

t_img = numpy.fft.fft2(pad_img)
t_img = numpy.fft.fftshift(t_img)
t_fil = numpy.fft.fft2(pad_fil)
t_fil = numpy.fft.fftshift(t_fil)
r_img = t_img * t_fil
r_img = numpy.fft.ifftshift(r_img)
r_img = numpy.absolute(numpy.fft.ifft2(r_img))

mini = numpy.min(r_img)
maxi = numpy.max(r_img)
for i in range(r1):
    for j in range(c1):
        r_img[i][j] = ((r_img[i][j]-mini)*255)/(maxi-mini)
r_img = numpy.uint8(r_img)
cv2.imshow("RESULT",r_img)
