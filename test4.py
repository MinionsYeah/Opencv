#读取视频每帧图像的灰度图，并输出
import cv2
import matplotlib.pyplot as plt
import numpy as np
vc=cv2.VideoCapture('video2.mp4')
#检查是否打开正确
if vc.isOpened():
    open,frame=vc.read()
else:
    open = False
while open:
    ret,frame=vc.read()
    if frame is None:
        break
    if ret == True:
        cv2.imshow('result',frame)
        if cv2.waitKey(33)==27:
            break
vc.release()
cv2.destroyAllWindows()