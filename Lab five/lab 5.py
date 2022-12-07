import numpy
import os
import cv2
import math

os.chdir("E:\LAB 5")
a = int(input("enter odd filter size"))
my_img = cv2.imread("Capture.png",0)
r,c = numpy.shape(my_img)
print(r,c)
m = math.ceil(a/2)
print(m)
my_img1 = numpy.zeros([m+r+m,m+c+m],numpy.uint8)
r1,c1 = numpy.shape(my_img1)
print(r1,c1)

for i in range(r):
    for j in range(c):
        my_img1[i+(m)][j+(m)] = my_img[i][j]

cv2.imshow("gg2",my_img1)

fltr = numpy.zeros([3,3],numpy.float)
fltr[0,0] = 0.0625
fltr[0,1] = 0.125
fltr[0,2] = 0.0625
fltr[1,0] = 0.125
fltr[1,1] = 0.25
fltr[1,2] = 0.125
fltr[2,0] = 0.0625
fltr[2,1] = 0.125
fltr[2,2] = 0.0625

rows = numpy.zeros([3,3],numpy.float)

for t in range(r):
    for s in range(c):
        rows[0,0] = my_img1[t-1][s-1]
        rows[0,1] = my_img1[t-1][s]
        rows[0,2] = my_img1[t-1][s+1]
        rows[1,0] = my_img1[t][s-1]
        rows[1,1] = my_img1[t][s]
        rows[1,2] = my_img1[t][s+1]
        rows[2,0] = my_img1[t+1][s-1]
        rows[2,1] = my_img1[t+1][s]
        rows[2,2] = my_img1[t+1][s+1]
        my_img1[t][s] = 0;
        for i in range(3):
            for j in range(3):
                my_img1[t][s] = my_img1[t][s] + fltr[i][j]*rows[i][j]

cv2.imshow("gg",my_img1)










