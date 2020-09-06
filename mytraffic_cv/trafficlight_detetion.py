import cv2
from PIL import Image
import os
from gui.PATH import trafficoutputpath

def check(input_path):
    img=cv2.imread(input_path)
    H=img.shape[0]
    w=img.shape[1]
  
    bmax=gmax=rmax=0
    for i in range(H):
        for j in range(w):
            b,g,r=img[i,j] 
            if b>bmax:
                bmax=b
            if g>gmax:
                gmax=g
            if r>rmax:
                rmax=r

    if rmax>gmax:
        if rmax>bmax:
            return True
        else:
            print("ok") 
    else:
        if gmax>bmax:
            return False
        else:
            print('ok')
            

def check1(input_path):
    img=cv2.imread(input_path)
    H=img.shape[0]
    w=img.shape[1]
  
    tf={'red':0,'green':0,'orange':0}
    for i in range(H):
        for j in range(w):
            b,g,r=img[i,j] 
            if b>tf['orange']:
                tf['orange']=b
            if g>tf['green']:
                 tf['green']=g
            if r>tf['red']:
                 tf['red']=r

    # if tf['red']>tf['green']:
    #     if tf['red']>tf['orange']:
    #         return "red"
    #     else:
    #         return "orange" 
    # else:
    #     if tf['green']>tf['orange']:
    #         return 'green'
    #     else:
    #         return "orange"
    if tf['red']>tf['green']:
        return "red"
    else:
         return 'green'
      



# a=check1("D:\\compete\\7\\detect_result\\cache\\traffic\\2.jpg")
# print(a)

