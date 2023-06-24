#同比例放缩读取和输出图像
import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg')
img=cv2.resize(img,(0,0),fx=1.5,fy=1.5)
print(img.shape)
cv_show('black hair,colored inner hair,girl',img)