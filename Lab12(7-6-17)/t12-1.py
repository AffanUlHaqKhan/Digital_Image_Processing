import numpy
import cv2
import matplotlib.pyplot as plt

my_img = cv2.imread('image3.png',0)
r,c = numpy.shape(my_img)
my_img1 = numpy.zeros((r,c),dtype=numpy.uint8)
LBP = numpy.zeros((r,c),dtype = numpy.uint8)
fil = numpy.zeros((8),dtype=numpy.uint8)

for i in range(1,r-1):
    for j in range(1,c-1):
        m=0
        if(my_img[i][j]>my_img[i-1][j-1]): fil[0]=1
        if(my_img[i][j]>my_img[i-1][j]): fil[1]=1
        if(my_img[i][j]>my_img[i-1][j+1]): fil[2]=1
        if(my_img[i][j]>my_img[i][j+1]): fil[3]=1
        if(my_img[i][j]>my_img[i+1][j+1]): fil[4]=1
        if(my_img[i][j]>my_img[i+1][j]): fil[5]=1
        if(my_img[i][j]>my_img[i+1][j-1]): fil[6]=1
        if(my_img[i][j]>my_img[i][j-1]): fil[7]=1
        
        for k in range(8):
            fil[k]=fil[k]*2**m
            m=m+1

        LBP[i][j]=numpy.sum(fil)

cv2.imshow('a',LBP)

arr = numpy.zeros(256)

for i in range(r):
    for j in range(c):
        arr[my_img[i][j]] = arr[my_img[i][j]]+1
plt.stem(arr)
plt.show()

bins = numpy.zeros(8)
z = 0
for i in range(8):
    bins[i] = numpy.sum(arr[z:z+32])
    z=z+32

plt.stem(bins)
plt.show()
