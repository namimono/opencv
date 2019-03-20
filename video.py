import cv2
import numpy as np

video=cv2.VideoCapture(0)
fps=24                                                  #视频每秒帧数
size=(int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
video_writer=cv2.VideoWriter('output2.avi',-1,fps,size)

success, fram = video.read()
numfram=3*fps                                     #视频总时间
while(success and numfram >0):

    fram=cv2.cvtColor(fram,cv2.COLOR_RGB2GRAY)
    fram = cv2.blur(fram, (3, 3))
    fram = cv2.Canny(fram, 10, 20)
    video_writer.write(fram)
    success, fram = video.read()
    numfram-=1
video.release()

