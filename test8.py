#图像平滑处理，滤波
import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg')
img1=cv2.blur(img,(5,5)) #均值模糊
img2=cv2.boxFilter(img,-1,(5,5),normalize=True)  #方框滤波
img3=cv2.GaussianBlur(img,(5,5),1) #高斯模糊
img4=cv2.medianBlur(img,5) #中值滤波
res=np.hstack((img2,img3,img4)) #图像拼接
cv_show('black hair,colored inner hair,girl',res)