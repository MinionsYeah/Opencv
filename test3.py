#读取并输出图像，最终再保存图像
import cv2
#import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img=cv2.imread('black hair,colored inner hair,girl.jpg')
print(img.shape)
cv_show('black hair,colored inner hair,girl',img)
cv2.imwrite('black hair,colored inner hair,girl.png',img)