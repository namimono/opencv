import cv2
import numpy as np

img=cv2.imread('2.jpg')
# 腐蚀图片
# element=cv2.getStructuringElement(cv2.MORPH_RECT,ksize=(5,5))
# dst=cv2.erode(img,element)

#blur
# img=img.astype(np.float32)
dst=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst=cv2.blur(dst,(3,3))
dst=cv2.Canny(dst,10,50)
cv2.imshow('yuan',img)
cv2.imshow('ss',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()