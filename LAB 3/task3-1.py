import numpy
import cv2
import os
import math

os.chdir("G:\lab # 3")

img = cv2.imread("gradient.png",0)
img = cv2.resize(img, (512,512))
r,c = numpy.shape(img)
a = input("enter the intensity division value in multiples of 2: ")
a = int(a)
col = math.floor(int(c/a))
q=col
ccount=0

count = int(256/a)
count1 = count-1

acount=1
for x in range(acount,a,1):
    for j in range(ccount,col):
        for k in range(r):
            img[k][j]=count1
    count1=count1+count
    print(count1)
    ccount=col+1
    print(ccount)
    col=col+q
    print(col)
    print(acount)

cv2.imshow("test",img)
