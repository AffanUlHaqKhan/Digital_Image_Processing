import numpy
import cv2
import os
import math

my_img=cv2.imread("c.tif",0)
r,c = numpy.shape(my_img)
print(r)
print(c)
label = 0
labellist = []
cclist = numpy.zeros((r,c), dtype = numpy.uint8)
cclist[0][0] = label
labellist.append(label)

for i in range (0,r): #labeling other rows with comparison to first row
    for j in range (0,c):
        if my_img[i,j] == my_img[i,j-1] and my_img[i-1,j] == my_img[i,j]: #
            if cclist[i,j-1] <= cclist[i-1,j]:
                cclist[i,j] = cclist[i,j-1]
                if cclist[i,j-1] != cclist[i-1,j]:
                    temp = cclist[i-1,j]
                    for y in range (0,r):
                        for z in range (0,c):
                            if cclist[y,z] == temp:
                                cclist[y,z]=cclist[i,j]
                    if temp in labellist:
                            labellist.remove(temp)                                         
            elif cclist[i,j-1] > cclist[i-1,j]:
                cclist[i,j] = cclist[i-1,j]
                temp=cclist[i,j-1]
                for y in range(0,r):
                    for z in range(0,c):
                        if cclist[y][z] == temp:
                            cclist[y][z]=cclist[i][j]
                if temp in labellist:
                    labellist.remove(temp)
        if my_img[i][j-1] == my_img[i][j]: #
            cclist[i][j] = cclist[i][j-1]
        if my_img[i-1][j] == my_img[i][j]: #
            cclist[i][j] = cclist[i-1][j]
        if my_img[i-1][j-1] == my_img[i][j]: #
            cclist[i][j] = cclist[i-1][j-1]
        if j < c-1:
            if my_img[i-1][j+1] == my_img[i][j]: #
                cclist[i][j] = cclist[i-1][j+1]
        if my_img[i][j-1] == my_img[i][j] and my_img[i-1][j]!=my_img[i][j]: #
            cclist[i][j] = cclist[i][j-1]
        if my_img[i][j-1] != my_img[i][j] and my_img[i-1][j]==my_img[i][j]: #
            cclist[i][j] = cclist[i-1][j]
        if my_img[i][j-1]!=my_img[i][j] and my_img[i-1][j]!=my_img[i][j]: #
            label = label+1
            labellist.append(label)
            cclist[i][j] = label
del labellist[0]      
print(len(labellist))

color = math.floor(256/(len(labellist)-1))

cclist = numpy.uint8(cclist)
cv2.imshow("a.jpg",cclist)
cv2.imwrite("a1.jpg",cclist)

            
                    
        
    
            
