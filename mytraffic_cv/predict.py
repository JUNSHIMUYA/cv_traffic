from nets.yolo3 import yolo_body
from keras.layers import Input
from yolo import YOLO
from PIL import Image,ImageDraw

yolo = YOLO()
trfn=0
carn=0
lrx=920
rrx=880
carnums=0
carlist=[]
while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image,i,m= yolo.detect_image(image,trfn,carn,lrx,rrx,carnums,carlist)
        draw = ImageDraw.Draw(r_image)
        draw.line((260,850,1500,850),fill='red',width=5)
        trfn=i
        carn=m
        r_image.show()

