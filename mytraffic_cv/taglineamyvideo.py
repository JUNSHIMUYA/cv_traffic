from keras.layers import Input
from yolo import YOLO
from PIL import Image
import numpy as np
import cv2
yolo = YOLO()

input_path="D:\\compete\\video-01.avi"
output_path="D:\\compete\\output"

Vreader=cv2.VideoCapture(input_path)
fps=Vreader.get(cv2.CAP_PROP_FPS)#获取视频帧率
width=int(Vreader.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(Vreader.get(cv2.CAP_PROP_FRAME_HEIGHT))
size=(width,height)

videoWirte=cv2.VideoWriter("D:\\compete\\output\\3.avi",  cv2.VideoWriter_fourcc(*'XVID'),fps,size) 

success,frame=Vreader.read()
i=0
n=0
while success:
    frame=cv2.line(frame,(800,300),(1300,300),(255,0,0),5)
    frame=cv2.line(frame,(360,700),(1500,700),(255,0,0),5)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # 转变成Image
    frame = Image.fromarray(np.uint8(frame))

    # 进行检测
    frame=yolo.detect_image(frame,i,n)
    i=0
    n=0
    frame = np.array(frame)

    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    videoWirte.write(frame)
    success,frame=Vreader.read() 
print("end!") 
    
    