import numpy
import os
import cv2

row = input ("Enter Rows: ")
col = input ("Enter Coloumns: ")
pad = input ("Enter Padding: ")

row = eval (row)
col = eval (col)
pad = eval (pad)

my_img = numpy.ones((pad+row+pad,pad+col+pad),dtype=numpy.uint8)
my_img = 255*my_img

blk = numpy.zeros((pad+row+pad,pad+col+pad),dtype=numpy.uint8)
blk = 0*blk

for i in range(pad):
    for j in range(pad+col+pad):
        my_img [i][j] = blk [i][j]
        my_img [-i][j] = blk [i][j]

for i in range(pad+row+pad):
    for j in range(pad):
        my_img [i][j] = blk [i][j]
        my_img [i][-j] = blk [i][j]        

cv2.imshow("Result",my_img)
