import numpy 
import cv2
import os
import math

row = input("Enter the width of white image box: ")
col = input("Enter the height of whiteimage box: ")

row = eval (row)
col = eval (col)

rc =math.floor((1/8)* row)

my_green = numpy.ones (( row, col,3 ),dtype=numpy.uint8)
my_green[ : ,0:rc] = (0,255,0)      
my_red = numpy.ones (( row, col,3 ),dtype=numpy.uint8)
my_red[ : ,0:rc] = (0,0,255)
my_blue = numpy.ones (( row, col,3 ),dtype=numpy.uint8)
my_blue[ : ,0:rc] = (255,0,0)

my_image = numpy.ones (( row, col,3 ),dtype=numpy.uint8)
my_image = my_image*255
my_zero = numpy.ones((row,col,3),dtype=numpy.uint8)
my_zero= my_zero*0


for i in range (rc):
    for j in range(rc):
        
            my_image[i][j]= my_green[i][j]
            my_image[-i][j]= my_red[i][j]
            my_image[i][-j]= my_blue[i][j]
            my_image[-i][-j]= my_zero[i][j]   
            
cv2.imshow("result",my_image)
