import cv2
import matplotlib.pyplot as plt
import numpy as np 
def cv_show(name,img):
    """显示图像"""
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
capture=cv2.VideoCapture(0)
while True:
    ret,frame = capture.read()
    cv2.imshow("camera",frame)
    key = cv2.waitKey(1)
    if key != -1:
        break
capture.release()