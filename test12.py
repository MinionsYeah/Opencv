#图像轮廓
import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg',cv2.IMREAD_GRAYSCALE)
ret,dst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
draw_img=img.copy()
res=cv2.drawContours(draw_img,contours,-1,(0,0,255),1)
cv_show('black hair,colored inner hair,girl',res)