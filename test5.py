import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg')
imgb=img.copy()
imgb[:,:,1]=0
imgb[:,:,2]=0
print(imgb)
cv_show('black hair,colored inner hair,girl',imgb)