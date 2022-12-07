import numpy
import cv2
import math

my_img = cv2.imread("broken_text.tif",0)
n = input("enter n")
n = int(n)
m = n
r,c = numpy.shape(my_img)
print(r,c)
my_img1 = numpy.zeros((r,c), dtype=numpy.double)
rect = cv2.getStructuringElement(cv2.MORPH_RECT,(n,m))
circle = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(n,m))
cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(n,m))

r1=math.floor(n/2)
c1=math.floor(m/2)
print(r1,c1)
s = numpy.sum(rect)
s1 = numpy.sum(circle)
s2 = numpy.sum(cross)
print(s,s1,s2)

for i in range(r1,r-r1):
    for j in range(c1,c-c1):
        st = i-r1
        temp = numpy.zeros((n,m), dtype = numpy.double)
        for k in range(n):
            ed = j-c1
            for l in range(m):
                temp[k][l] = rect[k][l]*my_img[st][ed]
                ed=ed+1
            st=st+1
        s3 = numpy.sum(temp)
        if s3 != s*255:
            my_img1[i][j] = s3
cv2.imshow("a",numpy.uint8(my_img1))
