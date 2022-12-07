import numpy
import os
import cv2
import math

my_img = cv2.imread("Fig02.tif",0)
arr = numpy.shape(my_img)

gamma =[0.6, 0.9, 1.3, 1.8]
length = len(gamma)
print(length)

def g_power(array,a):
    arr1 = numpy.shape(array)
    my_img1 = numpy.ones((arr1[0],arr1[1]), dtype = numpy.float64)
    for i in range (length):
        for x in range(arr[0]):
            for y in range(arr[1]):
                temp = my_img[x][y]**a
                my_img1[x][y]=temp
    return my_img1

def log_n(array):
    arr1 = numpy.shape(array)
    my_img2 = numpy.ones((arr1[0],arr1[1]), dtype = numpy.float64)
    for i in range(arr[0]):
        for j in range(arr[1]):
            temp = numpy.log10(array[i][j]+1)
            my_img2[i][j] = temp
    return my_img2

def normalize(array):
    arr1 = numpy.shape(array)
    my_img3 = numpy.ones((arr1[0],arr1[1]), dtype = numpy.float64)
    minimum = numpy.min(array)
    maximum = numpy.max(array)
    for i in range(arr[0]):
        for j in range(arr[1]):
            temp = ((array[i][j]-minimum)/(maximum-minimum))*255
            my_img3[i][j] = temp
    my_img3 = numpy.uint8(my_img3)
    return my_img3

for i in range (length):
    
    if i==3:
        a=g_power(my_img,gamma[i])
        my_img1 = numpy.uint8(a)
        cv2.imshow("1",my_img1)
        c = normalize(a)
        cv2.imshow("4",c)
        b=log_n(c)
        my_img2 = numpy.uint8(b)
        cv2.imshow("2",my_img2)
        
        
