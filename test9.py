#边缘处理
import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg',cv2.IMREAD_GRAYSCALE)
#Sobel算子
imgsobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
imgsobelx=cv2.convertScaleAbs(imgsobelx)
imgsobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
imgsobely=cv2.convertScaleAbs(imgsobely)
imgsobelxy=cv2.addWeighted(imgsobelx,0.5,imgsobely,0.5,0)
#Scharr算子
imgscharrx=cv2.Scharr(img,cv2.CV_64F,1,0)
imgscharrx=cv2.convertScaleAbs(imgscharrx)
imgscharry=cv2.Scharr(img,cv2.CV_64F,0,1)
imgscharry=cv2.convertScaleAbs(imgscharry)
imgscharrxy=cv2.addWeighted(imgscharrx,0.5,imgscharry,0.5,0)
#Laplacian算子
imglaplacian=cv2.Laplacian(img,cv2.CV_64F)
imglaplacian=cv2.convertScaleAbs(imglaplacian)
#图片对比
res=np.hstack((imgsobelxy,imgscharrxy,imglaplacian))
cv_show('black hair,colored inner hair,girl',res)