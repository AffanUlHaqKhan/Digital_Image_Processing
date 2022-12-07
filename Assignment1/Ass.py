import numpy
import os
import cv2
import math
import matplotlib.pyplot as plt

os.chdir("F:\Digital Image Processing EC-312\Assignment1")
my_img=cv2.imread("a.png",0)
r,c = numpy.shape(my_img)
my_img1 = numpy.ones((r,c), dtype = numpy.uint8)

#############################################################
#################Thresh Holding Image########################
mean = numpy.mean(my_img)
print(mean)
for i in range(r):
    for j in range(c):
        if my_img[i][j] < mean:
            my_img1[i][j]=0
        elif my_img[i][j] > mean:
            my_img1[i][j]=255

cv2.imshow("a",my_img1)
cv2.imwrite("a.png",my_img1)

label = 0
labellist = []
cclist = numpy.zeros((r,c), dtype = numpy.uint8)
cclist[0][0] = label
labellist.append(label)

###########################################################################
#################Connected Components/Objects Image########################
for i in range (0,r): #labeling other rows with comparison to first row
    for j in range (0,c):
        if my_img1[i,j] == my_img1[i,j-1] and my_img1[i-1,j] == my_img1[i,j]: #
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
        if my_img1[i][j-1] == my_img1[i][j]: #
            cclist[i][j] = cclist[i][j-1]
        if my_img1[i-1][j] == my_img1[i][j]: #
            cclist[i][j] = cclist[i-1][j]
        if my_img1[i-1][j-1] == my_img1[i][j]: #
            cclist[i][j] = cclist[i-1][j-1]
        if j < c-1:
            if my_img1[i-1][j+1] == my_img1[i][j]: #
                cclist[i][j] = cclist[i-1][j+1]
        if my_img1[i][j-1] == my_img1[i][j] and my_img1[i-1][j]!=my_img1[i][j]: #
            cclist[i][j] = cclist[i][j-1]
        if my_img1[i][j-1] != my_img1[i][j] and my_img1[i-1][j]==my_img1[i][j]: #
            cclist[i][j] = cclist[i-1][j]
        if my_img1[i][j-1]!=my_img1[i][j] and my_img1[i-1][j]!=my_img1[i][j]: #
            label = label+1
            labellist.append(label)
            cclist[i][j] = label
        
print(labellist)
print(len(labellist))
print(cclist)
cclist = numpy.uint8(cclist)
cv2.imshow("b.jpg",cclist)
cv2.imwrite("frst.jpg",cclist)

###################################################################
####################Objects Centre Image###########################
centersx = numpy.zeros(len(labellist))
centersy = numpy.zeros(len(labellist))
a = len(labellist)

for x in range(1,a):
    countr = 0
    countc = 0
    count = 0
    for i in range (0,r):
        for j in range (0,c):
            col=j
            pa = 0
            if cclist[i][j]==0:
                my_img1[i][j]=0
            if cclist[i][j]==labellist[x]:
                my_img1[i][j]=255
                countr += i
                countc = countc+col
                count += 1
    cx = round(countr/count)
    cy=round(countc/count)
    my_img1[cx][cy]=0
    centersx[x] = cx
    centersy[x] = cy
print(centersx)
print(centersy)
distance = []
xllist = []
yllist = []
imx = round(r/2)
imy = round(c/2)
print(imx)
print(imy)
print(len(centersx))
m=0
for i in range(1,len(centersx)):
    for j in range(i+1,len(centersx)):
        s = round(abs(math.sqrt((centersx[j]-centersx[i])**2+(centersy[j]-centersy[i])**2)))
        distance.append(s)
        xllist.append(labellist[i])
        yllist.append(labellist[j])
print(distance)
print(xllist)
print(yllist)
m=0
lx=0
ly=0
my_img2 = my_img1
for x in range (len(distance)):
    if distance[x] > m:
        m = distance[x]
        lx = xllist[x]
        ly = yllist[x]
    for i in range(r):
        for j in range(c):
            if cclist[i][j] == lx or cclist[i][j] == ly:
                my_img2[i][j] = 0
                                          
cv2.imshow("c.jpg",my_img2)

###################################################################
#####################Object Shapes and Groups######################

im,contours,hierarchy = cv2.findContours(my_img1,cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)

contours.pop(0)
print(len(contours))
shapes = []
groups = [[],[],[]]
for c in contours:
    
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    approx = cv2.approxPolyDP(c,0.005*cv2.arcLength(c,True),True)
    print(approx)

 
    # draw the contour and center of the shape on the image
    #cv2.drawContours(my_img1, [c], 0,255, 0)
    #cv2.circle(my_img1, (cX, cY), 1, 255, -1)
    if(len(approx)==4):
        shapes.append("4 sided Polygon")
        groups[0] = ("4 sided Polygon")
    if (len(approx)>10):
        ellipse = cv2.fitEllipse(c)
        center,axes,orientation = ellipse
        major_axis = max(axes)
        minor_axis = min(axes)
        eccentricity = numpy.sqrt(1-(minor_axis/major_axis)**2)
        if (eccentricity < 0.4):
            shapes.append("Circle")
            groups[1] = ("Circle")
        else:
            shapes.append("irregular shape")
            groups[2] = ("irregular shape")

print(shapes)
print(groups)
#cv2.imshow("Image", my_img1)

###################################################################
########################intensities################################

r1,c1 = numpy.shape(my_img1)
for i in range(0,len(groups)):
        mask = numpy.zeros((r1,c1), dtype=numpy.uint8) *255
        intensities=[]
        for j in range(0,len(groups[i])):
            cnt=contours[groups[i][j]]
            cv2.drawContours(mask, [cnt], -1, 255, -1)
            intensities.append(numpy.mean(mask))
        if(all(intensities[0] == item for item in intensities)):
            print ("Equal intensities")
        else:
            print ("Unequal intensities")

        temporary = cv2.bitwise_and(imgray, mask, mask=mask)
        cv2.imwrite("ola"+str(i)+".png",temporary)

