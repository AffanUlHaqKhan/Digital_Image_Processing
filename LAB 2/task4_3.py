import numpy
import cv2
import os
import math

row = input("Enter the width of white image box: ")
col = input("Enter the height of whiteimage box: ")
pad = input("Enter Padding Size not more than 30px:")

row1 = input("Enter number of rows:")
col1 = input("Enter number of coloumns:")

row = eval (row)
col = eval (col)
pad = eval (pad)
row1 = eval (row1)
col1 = eval (col1)

my_img = numpy.ones((row,col),dtype=numpy.uint8)
my_img = my_img*255
my_img1 = numpy.zeros((row,col),dtype=numpy.uint8)
my_img1 = my_img*0
row_div = math.floor(row/(row1+1))
col_div = math.floor(col/(col1+1))

count_row = row_div - (math.floor(pad/2))
count_col = col_div - (math.floor(pad/2))


for i in range (1,row1+1):
    a=i*count_row
    b=i*(count_row)+pad
    for x in range(a,b):
        for j in range(col):
            my_img [x][j] = my_img1 [x][j]


for i in range (1,col1+1):
    a=i*count_col
    b=i*(count_col)+pad
    for x in range(row):
        for j in range(a,b):
            my_img [x][j] = my_img1 [x][j]
            

cv2.imshow("Result",my_img)
