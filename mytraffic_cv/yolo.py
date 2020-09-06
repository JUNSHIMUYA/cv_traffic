import os
import numpy as np
import copy
import colorsys
from timeit import default_timer as timer
from keras import backend as K
from keras.models import load_model
from keras.layers import Input
from PIL import Image, ImageFont, ImageDraw
from nets.yolo3 import yolo_body,yolo_eval
from utils.utils import letterbox_image
from trafficlight_detetion import check,check1
from lprcmd import cartag
import cv2
from gui.PATH import Road_ROOTpath,normalcaridpath,caroutputpath,trafficoutputpath,resultpath,run_a_red_lightpath,run_a_red_light_img_path,caridpath,model_path,classes_path,anchors_path
class YOLO(object):
    _defaults = {
        "model_path": model_path,
        "anchors_path": anchors_path,
        "classes_path": classes_path,
        "score" : 0.5,
        "iou" : 0.3,
        "model_image_size" : (416, 416)
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    #---------------------------------------------------#
    #   初始化yolo
    #---------------------------------------------------#
    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        self.class_names = self._get_class()
        self.anchors = self._get_anchors()
        self.sess = K.get_session()
        self.boxes, self.scores, self.classes = self.generate()
        

    #---------------------------------------------------#
    #   获得所有的分类
    #---------------------------------------------------#
    def _get_class(self):
        classes_path = os.path.expanduser(self._defaults["classes_path"])
        with open(classes_path) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        return class_names

    #---------------------------------------------------#
    #   获得所有的先验框
    #---------------------------------------------------#
    def _get_anchors(self):
        anchors_path = os.path.expanduser(self._defaults["anchors_path"])
        with open(anchors_path) as f:
            anchors = f.readline()
        anchors = [float(x) for x in anchors.split(',')]
        return np.array(anchors).reshape(-1, 2)

    #---------------------------------------------------#
    #   获得所有的分类
    #---------------------------------------------------#
    def generate(self):
        model_path = os.path.expanduser(self._defaults["model_path"])
        assert model_path.endswith('.h5'), 'Keras model or weights must be a .h5 file.'
        
        # 计算anchor数量
        num_anchors = len(self.anchors)
        num_classes = len(self.class_names)

        # 载入模型，如果原来的模型里已经包括了模型结构则直接载入。
        # 否则先构建模型再载入
        try:
            self.yolo_model = load_model(model_path, compile=False)
        except:
            self.yolo_model = yolo_body(Input(shape=(None,None,3)), num_anchors//3, num_classes)
            self.yolo_model.load_weights(self._defaults["model_path"])
        else:
            assert self.yolo_model.layers[-1].output_shape[-1] == \
                num_anchors/len(self.yolo_model.output) * (num_classes + 5), \
                'Mismatch between model and given anchor and class sizes'

        print('{} model, anchors, and classes loaded.'.format(model_path))

        # 画框设置不同的颜色
        hsv_tuples = [(x / len(self.class_names), 1., 1.)
                      for x in range(len(self.class_names))]
        self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
        self.colors = list(
            map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)),
                self.colors))

        # 打乱颜色
        np.random.seed(3000)
        np.random.shuffle(self.colors)
        np.random.seed(None)

        self.input_image_shape = K.placeholder(shape=(2, ))

        boxes, scores, classes = yolo_eval(self.yolo_model.output, self.anchors,
                num_classes, self.input_image_shape,
                score_threshold=self._defaults["score"], iou_threshold=self._defaults["iou"])
        return boxes, scores, classes

    #---------------------------------------------------#
    #   检测图片
    #---------------------------------------------------#
    def detect_image(self, image,trfn,carn,lrx,rrx,carnums,carlist,sy,slx, srx,lx,ly):
        run_a_red_light=0
        totalcarn=0
        #list_num=len(carlist)
        #start = timer()
        # 调整图片使其符合输入要求
        new_image_size = (self._defaults["model_image_size"][0],self._defaults["model_image_size"][1])
        boxed_image = letterbox_image(image, new_image_size)
        image_data = np.array(boxed_image, dtype='float32')
        image_data /= 255.
        image_data = np.expand_dims(image_data, 0)  # Add batch dimension.

        # 预测结果
        
        
        
        out_boxes, out_scores, out_classes = self.sess.run(
            [self.boxes, self.scores, self.classes],
            feed_dict={
                self.yolo_model.input: image_data,
                self.input_image_shape: [image.size[1], image.size[0]],
                # K.learning_phase(): 0
            })
      
        print('Found {} boxes for {}'.format(len(out_boxes), 'img'))
      
        font = ImageFont.truetype('font/simhei.ttf',28)
        

        
        for i ,c in list(enumerate(out_classes)): 
            if i==1:

                trfn=trfn+1
                outputpath=trafficoutputpath
                img=image.crop((lx-15 , ly-30 , lx+15 , ly+30))
                img.save(outputpath+str(trfn)+".jpg")
                temp=check1(outputpath+str(trfn)+".jpg")
                draw = ImageDraw.Draw(image)

                if temp=='red':

                    draw.rectangle((lx-15 , ly-30 , lx+15 , ly+30),outline="red",width=2)
                    draw.rectangle((lx-15 , ly-55 , lx+70 , ly-30),fill="white")
                    draw.text((lx-15 , ly-55 ), "red", fill=(0, 0, 0), font=font)
      
                    f1=open(resultpath, "a", encoding='utf-8')
                    f2=open(run_a_red_lightpath(), "a", encoding='utf-8') 
                    f3=open(Road_ROOTpath()+'all_illegal_car_info.txt', "a+", encoding='utf-8') 
                    for cn ,cf in list(enumerate(out_classes)):
                        if cf!=2:
                            continue
                                
                        predicted_class = self.class_names[cf]
                        box = out_boxes[cn]
                        score = out_scores[cn]

                        top, left, bottom, right = box
                        top = top - 5
                        left = left - 5
                        bottom = bottom + 5
                        right = right + 5

                        top = max(0, np.floor(top + 0.5).astype('int32'))
                        left = max(0, np.floor(left + 0.5).astype('int32'))
                        bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
                        right = min(image.size[0], np.floor(right + 0.5).astype('int32'))
                            # 画框框
                        label = '{} {:.2f}'.format(predicted_class, score)
                        draw = ImageDraw.Draw(image)
                        label_size = draw.textsize(label, font)
                        label = label.encode('utf-8')

                        if top - label_size[1] >= 0:
                            text_origin = np.array([left, top - label_size[1]])
                        else:
                            text_origin = np.array([left, top + 1])

                        x=left
                        y1=top
                        y2=bottom
                        if cf==2 and x<srx and (x>slx and y2<1080) and y1>500 :
                            carn=carn+1
                            
                            car_outputpath=caroutputpath
                            img=image.crop((left , top , right , bottom ))
                            img.save(car_outputpath+str(carn)+".jpg") 
                            # if  y>500 :
                            ch=cartag(car_outputpath+str(carn)+".jpg")
                        
                            f1.write(ch+"\n")
                            draw.rectangle(
                                    (left , top , right , bottom ),
                                    outline=self.colors[cf],width=2)
                            draw.rectangle(
                                    [tuple(text_origin), tuple(text_origin + label_size)],
                                    fill=self.colors[cf])
                            draw.text(text_origin, str(label,'UTF-8'), fill=(0, 0, 0), font=font)

                            draw.rectangle(
                                    (right , top , right+150 , top+40),
                                    fill=self.colors[cf])
                            draw.text((right , top , right+30 , top+60), ch, fill=(0, 0, 0), font=font)
                            if ((top+bottom)/2-50)<sy:
                                if ch is not '00000' and ch[1] is not '1' :
                                    f3.write(ch+" 闯红灯"+"\n")
                                    f2.write(ch+" 闯红灯"+"\n")
                                    run_a_red_light+=1
                                draw.rectangle(
                                    (right , top+40, right+100 , top+80),
                                    fill='red')
                                draw.text((right , top+40, right+60 , top+140), "闯红灯", fill=(0, 0, 0), font=font)
                                if ch is not '00000' and ch[1] is not '1' :
                                    image.save(run_a_red_light_img_path()+ch+'_闯红灯'+".jpg")
                    # f3.close()                    
                    # f2.close()
                    # f1.close()
                else:
                    draw.rectangle(
                    (lx-15 , ly-30 , lx+15 , ly+30),
                    outline="green",width=2)
                    draw.rectangle(
                    (lx-15 , ly-55 , lx+70 , ly-30),
                    fill="white")
                    draw.text((lx-15 , ly-55 ), "green", fill=(0, 0, 0), font=font)    
                del draw            
                  


            if c==9:
                continue
            
            predicted_class = self.class_names[c]
            box = out_boxes[i]
            score = out_scores[i]

            top, left, bottom, right = box
            top = top - 5
            left = left - 5
            bottom = bottom + 5
            right = right + 5

            top = max(0, np.floor(top + 0.5).astype('int32'))
            left = max(0, np.floor(left + 0.5).astype('int32'))
            bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
            right = min(image.size[0], np.floor(right + 0.5).astype('int32'))

            # 画框框
            label = '{} {:.2f}'.format(predicted_class, score)
            draw = ImageDraw.Draw(image)
            label_size = draw.textsize(label, font)
            label = label.encode('utf-8')
           
            if top - label_size[1] >= 0:
                text_origin = np.array([left, top - label_size[1]])
            else:
                text_origin = np.array([left, top + 1])

            draw.rectangle(
                    (left , top , right , bottom ),
                    outline=self.colors[c],width=2)
            draw.rectangle(
                [tuple(text_origin), tuple(text_origin + label_size)],
                fill=self.colors[c])
            draw.text(text_origin, str(label,'UTF-8'), fill=(0, 0, 0), font=font)

          
           
            if top - label_size[1] >= 0:
                text_origin = np.array([left, top - label_size[1]])
            else:
                text_origin = np.array([left, top + 1])

            draw.rectangle(
                    (left , top , right , bottom ),
                    outline=self.colors[c],width=2)
            draw.rectangle(
                [tuple(text_origin), tuple(text_origin + label_size)],
                fill=self.colors[c])
            draw.text(text_origin, str(label,'UTF-8'), fill=(0, 0, 0), font=font)

            if c==2 or c==3 or c==5 or c==7:
                totalcarn+=1
            del draw

            
            if c==2 and bottom>950 and left>slx:
                carnums+=1
                img=image.crop((left , top , right , bottom ))
                img.save(caridpath+str(carnums)+'.jpg') 
                carid=cartag(caridpath+str(carnums)+'.jpg')
                draw = ImageDraw.Draw(image)
                draw.rectangle((right , top , right+150 , top+40),fill="green")
                draw.text((right , top , right+30 , top+60), carid, fill=(0, 0, 0), font=font)
                
                if carid in carlist:
                    continue
                else:
                    if carid!='00000' and len(carid)==7:
                        carlist.append(carid)
            
        
            
        draw = ImageDraw.Draw(image)
        draw.rectangle(
                (1300,150,1900,200),
                fill="white")
        draw.text((1300,160,1900,180), "路口通过car的数量为:"+str(len(carlist)), fill="black",font=font) 

        del draw     

        draw = ImageDraw.Draw(image)
        draw.rectangle(
                (1300,50,1900,140),
                fill="white")
        if totalcarn>=10:
            draw.text((1300,60,1900,100), "当前路口机动车数量为"+str(totalcarn)+"大于9"+"  拥堵", fill="black",font=font) 
        else:
            draw.text((1300,60,1800,100), "当前路口机动车数量："+str(totalcarn), fill="black",font=font) 
        draw.text((1300,100,1800,140), "当前路口闯红灯数量："+str(run_a_red_light), fill="black",font=font)


        del draw
        return image,trfn,carn,carnums,len(carlist), run_a_red_light,totalcarn 

    def close_session(self):
        self.sess.close()
        