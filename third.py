import cv2
import numpy as np

from scipy import ndimage

def onTrackbar(a):
    print(a)
# kernel_3x3=np.array([[-1,-1,-1],
#                      [-1,8,-1],
#                      [-1,-1,-1]])
# img=cv2.imread('2.jpg',0)
# k3=ndimage.convolve(img,kernel_3x3)
#
# blurred=cv2.GaussianBlur(img,(11,11),1)
# g_hpf = img - blurred
# cv2.imshow('ke',k3)
img=cv2.imread('2.jpg',1)
cv2.namedWindow("window",cv2.WINDOW_NORMAL)
cv2.createTrackbar("blur","window",1,100,onTrackbar)

while(1):
    b=cv2.getTrackbarPos("blur","window")
    if(b!=0):

        nimg=cv2.blur(img,(b,b))
        cv2.imshow("window", nimg)
        cv2.waitKey(0)
    else:
        cv2.imshow("window", img)
        cv2.waitKey(0)


cv2.destroyAllWindows()


