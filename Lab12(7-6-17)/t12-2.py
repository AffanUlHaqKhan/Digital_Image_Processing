import numpy 
import cv2
import matplotlib.pyplot as plt
from skimage import feature

my_img = cv2.imread('image1.png',0)
my_img1 = cv2.imread('image2.png',0)
my_GLCM =feature.greycomatrix(my_img,[0],[0], levels=None,symmetric=False, normed=False)
my_GLCM1 =feature.greycomatrix(my_img1,[0],[0], levels=None,symmetric=False, normed=False)

my_property = feature.greycoprops(my_GLCM1, prop='homogeneity')
print('Homogeniety = ',my_property)
my_property = feature.greycoprops(my_GLCM1, prop='contrast')
print('Contrast = ',my_property)
my_property = feature.greycoprops(my_GLCM1, prop='energy')
print('Energy',my_property)
my_property = feature.greycoprops(my_GLCM1, prop='dissimilarity')
print('Dissimilarity = ',my_property)

my_property = feature.greycoprops(my_GLCM, prop='homogeneity')
print('Homogeniety = ',my_property)
my_property = feature.greycoprops(my_GLCM, prop='contrast')
print('Contrast = ',my_property)
my_property = feature.greycoprops(my_GLCM, prop='energy')
print('Energy = ',my_property)
my_property = feature.greycoprops(my_GLCM, prop='dissimilarity')
print('Dissimilarity = ',my_property)