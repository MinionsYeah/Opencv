#Canny边缘检测
#cv2.Canny(处理的内容，minVal,maxVal)
import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('building.jpg',cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img,(0,0),fx=0.2,fy=0.2)
v1=cv2.Canny(img,170,270)
v2=cv2.Canny(img,50,100)
#效果对比
res=np.hstack((v1,v2))
cv_show('building.jpg',res)