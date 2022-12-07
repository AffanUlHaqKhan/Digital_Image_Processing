import numpy
import os
import cv2
import math
import matplotlib.pyplot as plt

my_img = cv2.imread("fig01.tif",0)
r,c = numpy.shape(my_img)
cv2.imshow("Original",my_img)
gll = numpy.zeros(256)
length = len(gll)
pdf = numpy.zeros(length)
cdf = numpy.zeros(length)
enh = numpy.zeros(length)
for i in range(r):
    for j in range(c):
        temp = my_img[i][j]
        count = gll[temp]
        count = count+1
        gll[temp] = count

print(gll)
plt.plot(gll)
plt.xlabel ( "intensity value")
plt.ylabel ( "intensity count")
plt.show()

length = len(gll)
pdf = numpy.zeros(length)
for i in range(length):
    temp = gll[i]
    count = temp / (r*c)
    pdf[i] = count

print(pdf)
plt.plot(pdf)
plt.xlabel ( "intensity value")
plt.ylabel ( "intensity count")
plt.show()

for i in range(length):
    cdf[i] = cdf[i-1] + pdf[i]

print(cdf)
plt.plot(cdf)
plt.xlabel ( "intensity value")
plt.ylabel ( "intensity count")
plt.show()

tf = 255*cdf
print (tf)

for i in range(r):
    for j in range(c):
        temp = my_img[i][j]
        temp1 = tf[temp]
        my_img[i][j] = temp1

cv2.imshow("out",my_img)


