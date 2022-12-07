import numpy
import cv2
import math
my_img=cv2.imread("fig02.jpg",0)
r,c= numpy.shape(my_img)
C = [52,155,249]

while True:
    C1_l=[]
    C2_l=[]
    C3_l=[]
    for i in range(r):
        for j in range(c):
            dist_1=numpy.abs(C[0]-my_img[i][j])
            dist_2=numpy.abs(C[1]-my_img[i][j])
            dist_3=numpy.abs(C[2]-my_img[i][j])
            if dist_1 < dist_2 and dist_1 < dist_3:
                C1_l.append(my_img[i][j])
            elif dist_2 < dist_1 and dist_2 < dist_3:
                C2_l.append(my_img[i][j])
            elif dist_3 < dist_2 and dist_3 < dist_1:
                C3_l.append(my_img[i][j])
    C1=C[0]
    C2=C[1]
    C3=C[2]
    C[0]=int(numpy.mean(C1_l))
    C[1]=int(numpy.mean(C2_l))
    C[2]=int(numpy.mean(C3_l))

    if C[0] in range(C1-1,C1+1)and C[1] in range(C2-1,C2+1) and C[2] in range(C3-1,C3+1):
        break
    
for i in range(r):
    for j in range(c):
        if my_img[i][j] in C1_l:
            my_img[i][j]= 0
        elif my_img[i][j] in C2_l:
            my_img[i][j]= 128
        elif my_img[i][j] in C3_l:
            my_img[i][j]=255
    
cv2.imshow("Res",my_img)
