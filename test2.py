#读取图像的灰度图，并输出
import cv2
import matplotlib.pyplot as plt
import numpy as np 
img=cv2.imread('black hair,colored inner hair,girl.jpg',cv2.IMREAD_GRAYSCALE)
print(img)
cv2.imshow('black hair,colored inner hair,girl',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ctrl + P
# select interpreter


# ctrl + F5