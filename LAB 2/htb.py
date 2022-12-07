import numpy as np
import cv2
import os
os.chdir("")
my=cv2.imread("Capture.png",0)
r=4;

size=np.shape(my)
my1 = cv2.resize(my,(size[1]*r,size[0]*r))

cv2.imwrite("out",my1)
