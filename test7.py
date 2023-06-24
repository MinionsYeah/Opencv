#阈值处理
import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg')
ret,dst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv_show('black hair,colored inner hair,girl',dst)

#cv2.threshold(要处理的图像，阈值，最大值，阈值处理的类型)
#THRESH_BINARY 大于阈值的部分取最大值，否则取0
#THRESH_BINARY_INV 与THRESHOLD_BINARY相反
#THRESH_TRUNC 大于阈值的部分设为阈值，否则不变
#THRESH_TOZERO 大于阈值的部分不改变，小于的部分取0
#THRESH_TOZERO_INV 与THRESHOLD_TOZERO 相反