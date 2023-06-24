# 直方图
import cv2
import matplotlib.pyplot as plt
import numpy as np 
img=cv2.imread('black hair,colored inner hair,girl.jpg',cv2.IMREAD_GRAYSCALE)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
print(hist.shape)
plt.hist(img.ravel(),256)
plt.show()