import numpy 
import cv2
import math

my_img=cv2.imread("Fig02.jpg",0)
my_img1=cv2.imread("Fig02.jpg",0)
r,c = numpy.shape(my_img)
my_img2 = numpy.zeros((r,c),dtype=numpy.double)
seed = 250
e=5
maxi=0
mini =255

while(numpy.sum(numpy.abs(my_img2-my_img1))!=0):
    my_img2 =numpy.zeros((r,c))+ my_img1
    for x in range(r):
        for y in range(c):
            if my_img1[x][y] == seed:
                if x+1<r and my_img[x][y] > my_img[x+1,y]-e and my_img[x][y] < my_img[x+1,y]+e:
                    my_img1[x+1,y] = seed
                
                elif x-1>=0 and my_img[x][y] > my_img[x-1,y]-e and my_img[x][y] < my_img[x-1,y]+e:
                    my_img1[x-1,y] = seed
                    
                elif y+1<c and my_img[x][y] > my_img[x,y+1]-e and my_img[x][y] < my_img[x,y+1]+e:
                    my_img1[x,y+1] = seed
                    
                elif y-1>=0 and my_img[x][y] > my_img[x,y-1]-e and my_img[x][y] < my_img[x,y-1]+e:
                    my_img1[x,y-1] = seed

                    
                elif y-1>=0 and x-1>=0 and my_img[x][y] > my_img[x-1,y-1]-e and my_img[x][y] < my_img[x-1,y-1]+e:
                    my_img1[x-1,y-1] = seed
                    
                elif y+1<c and x+1<r and my_img[x][y] > my_img[x+1,y+1]-e and my_img[x][y] < my_img[x+1,y+1]+e:
                    my_img1[x+1,y+1] = seed


                elif y+1<c and x-1>=0 and my_img[x][y] > my_img[x-1,y+1]-e and my_img[x][y] < my_img[x-1,y+1]+e:
                    my_img1[x-1,y+1] = seed
                    
                elif y+1<c and x-1>=0 and my_img[x][y] > my_img[x-1,y+1]-e and my_img[x][y] < my_img[x-1,y+1]+e:
                    my_img1[x-1,y+1] = seed
for x in range(r):
    for y in range(c):
        if my_img1[x][y] == seed:
            my_img1[x][y]=255
        else:
            my_img1[x][y]=0
for i in range(x):
    for j in range (y):
        if my_img1[i][j] > maxi:
            maxi = my_img1[i][j]
        if mini > my_img1[i][j]:
            mini = my_img1[i][j]
for i in range(x):
    for j in range (y):
        my_img1[i][j]=255*(my_img1[i][j]-mini)/(maxi-mini)
my_img1 = numpy.uint8(my_img1)
cv2.imshow("out",my_img1)
