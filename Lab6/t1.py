import numpy
import cv2
import os
import math


my_img = cv2.imread("Fig01.tif",0)
r,c = numpy.shape(my_img)
print(r,c)
a = input("input odd val for filter, r and c would be same")
a= int(a)
arr = numpy.ones((a,a),dtype = numpy.uint8)

r1 = math.floor(a/2)
c1 = math.floor(a/2)
r2 = math.ceil(a/2)
c2 = math.ceil(a/2)

min_img = numpy.ones((r,c),dtype = numpy.uint8)
min_img = 255*min_img
max_img = numpy.ones((r,c),dtype = numpy.uint8)
max_img = 255*max_img
mid_img = numpy.ones((r,c),dtype = numpy.uint8)
mid_img = 255*mid_img

for i in range(r1,r-r1):
    for j in range(c1,c-c1):
        z = 0
        e = []
        for x in range(i-r1,i+r2):
            t = 0
            for y in range(j-c1,j+c2):
                arr[z][t] = my_img[x][y]
                t = t+1
            z=z+1
        mini = numpy.amin(arr)
        min_img[i][j]=mini
        ma = numpy.amax(arr)
        max_img[i][j]=ma
        mi = numpy.ravel(arr)
        mid=numpy.median(mi)
        mid_img[i][j]=mid
    
r2,c2 = numpy.shape(min_img)
print(r2,c2)
cv2.imshow("a",min_img)
cv2.imshow("b",max_img)
cv2.imshow("c",mid_img)
