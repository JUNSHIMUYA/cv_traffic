import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont
frame=cv2.imread("D:\\compete\\JPEGimages\\1.jpg")
frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
frame = Image.fromarray(np.uint8(frame))
font = ImageFont.truetype('./font/platech.ttf',24)
draw = ImageDraw.Draw(frame)
draw.rectangle(
            (976.8-15 , 159.84-15 , 976.8+15 , 159.84+15),
            outline="orange",width=2)
#label_size = draw.textsize("orange")
draw.rectangle(
            (976.8-15 , 159.84-40 , 976.8+70 , 159.84-15),
            fill="white")
draw.text((976.8-15, 159.84-40), "orange", fill=(0, 0, 0),font=font)
draw.line((100,100,150,100),"red")
frame.show()

# import matplotlib.pyplot as plt
# X=["2s","4s","6s","8s","10s","12s","14s"]
# y=[10,11,22,34,34,22,23]

# plt.figure(figsize=(15,7))
# plt.plot(X,y,label='当前路口机动车数量')

# # 对应x轴与字符串
# plt.xticks(fontsize=30)
# plt.yticks(fontsize=30)
# plt.legend(fontsize=30)
# plt.xlabel('时间',fontsize=20)
# plt.ylabel('数量',fontsize=30)
# plt.title("路口车辆情况统计图",fontsize=30)
# plt.show()