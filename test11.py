#图像金字塔
import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg')
print(img.shape)
upimg=cv2.pyrUp(img)
downimg=cv2.pyrDown(upimg)
print(downimg.shape)
res=np.hstack((img,downimg))
cv_show('black hair,colored inner hair,girl',res)
#laplacian金字塔
Laplacian=img-downimg
cv_show('black hair,colored inner hair,girl',Laplacian)