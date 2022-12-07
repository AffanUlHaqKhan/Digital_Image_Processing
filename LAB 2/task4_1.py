import numpy
import cv2
import os

row = input("Enter the width of white image box: ")
col = input("Enter the height of whiteimage box: ")

row1 = input("Enter the width of black padding:")
col1 = input("Enter the height of black padding:")

row = eval (row)
col = eval (col)
row1 = eval (row1)
col1 = eval (col1)

my_img = numpy.ones((row,col),dtype=numpy.uint8)
my_img = 255*my_img

my_img1 = numpy.ones((row,col),dtype=numpy.uint8)
my_img1 = 0*my_img1

for i in range(row1):
    for j in range(col):
        my_img [i][j] = my_img1 [i][j]
        my_img [-i][j] = my_img1 [i][j]

for i in range(row):
    for j in range(col1):
        my_img [i][j] = my_img1 [i][j]
        my_img [i][-j] = my_img1 [i][j]        

cv2.imshow("Result",my_img)
