import numpy
import cv2
import os

my_img=cv2.imread("fig02.tif",0)
r,c = numpy.shape(my_img)
cv2.imshow('in',my_img)

img, mask = cv2.threshold(my_img, 10, 255, cv2.THRESH_BINARY)
im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    gray=cv2.drawContours(mask,[cnt],0,255,-1)


cv2.imshow('a',gray)

