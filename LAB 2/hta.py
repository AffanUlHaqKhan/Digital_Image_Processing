import numpy as np
import cv2
import os
os.chdir("")
my=cv2.imread("Capture.png",0)
r=16;

size=np.shape(my)
my1 = np.zeros((size[0]*r,size[1]*r))
for i in range(0,size[0]*r):
    for j in range (0,size[1]*r):
        my1[i,j]=my[np.int16(i/r),np.int16(j/r)]
cv2.imwrite("test",my1)
