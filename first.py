import cv2
import numpy as np
# img0=np.zeros((2,2,3),dtype=np.uint8)
# print(img0)
img=cv2.imread('4_48.jpeg',1)
# img0.itemset((37,37,0),123)
img[:,:,1]=0
cv2.imshow('img',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
#
# cv2.imshow("image",img)
# cv2.waitKey(0)
# # cv2.imwrite('1.jpeg',img)
# cv2.destroyAllWindows()