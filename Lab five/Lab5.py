import numpy
import cv2
def bless():
    im1 = cv2.imread("Capture.png",0)
    n=int(input("Enter dimension of filter = "))
    size = numpy.shape(im1)
    filt=numpy.ones((n,n),dtype = numpy.uint8)
    ffilter = filt* (1/(n*n))
    port=numpy.zeros((n,n),dtype = numpy.uint8)
    new = numpy.array(port)
    print(ffilter)
    
    z = int(numpy.floor(n/2))
    for i in range(z,size[0]-z):
        for j in range(z,size[1]-z):
            port = im1[i-z:i+z+1,j-z:j+z+1]
            new = port*ffilter
            im1[i,j]= sum(sum(new))
    cv2.imshow("lab5 1",im1)

def border():
    im1 = cv2.imread("Capture.ng",0)
    n=int(input("Enter dimension of filter = "))
    size = numpy.shape(im1)
    filt=numpy.ones((n,n),dtype = numpy.uint8)
    ffilter = filt* (1/(n*n))

    port=numpy.zeros((n,n),dtype = numpy.uint8)
    new = numpy.array(port)
    z = int(numpy.floor(n/2))
    
    r = size[0] + (2*z)
    c = size[1] + (2*z)
    

    im2 = numpy.zeros((r,c),dtype = numpy.uint8)

    for i in range (z,size[0]+z):
        for j in range (z,size[1]+z):
            im2[i,j]=im1[i-z,j-z]
    cv2.imshow("asdad", im2)
    

    print(ffilter)
    
    
    for i in range(z,r-z):
        for j in range(z,c-z):
            port = im2[i-z:i+z+1,j-z:j+z+1]
            new = port*ffilter
            im2[i,j]= sum(sum(new))
    cv2.imshow("lab5 1",im2)
    
def gfilter():
    im1 = cv2.imread("Capture.png",0)
    
    size = numpy.shape(im1)
    ffilter=[[0.0625, 0.125, 0.0625 ],[0.0125, 0.25, 0.125],[0.0625, 0.125, 0.0625 ]]
    port=numpy.zeros((3,3),dtype = numpy.uint8)
    new = numpy.array(port)
    print(ffilter)
    
    z = 1
    for i in range(z,size[0]-z):
        for j in range(z,size[1]-z):
            port = im1[i-z:i+z+1,j-z:j+z+1]
            new = port*ffilter
            im1[i,j]= sum(sum(new))
    cv2.imshow("lab5 1",im1)

