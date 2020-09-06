#-------------------------------------#
#       调用摄像头检测
#-------------------------------------#
from PIL import Image,ImageDraw,ImageFont
import numpy as np
import cv2
import matplotlib.pyplot as plt
from gui.PATH import infomation_path

def detect2(video_inputpath,video_outpath,light_Pos):
   
    
    import keras
    from yolo import YOLO
    
    yolo = YOLO()
    print("++++++++++++++++++",yolo.__str__())
    
    video_inp = video_inputpath
    video_out = video_outpath 
    video_reader = cv2.VideoCapture(video_inp)
    frame_h =int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_w = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    fps=video_reader.get(cv2.CAP_PROP_FPS)#获取视频帧率
    video_writer = cv2.VideoWriter(video_out,
                                cv2.VideoWriter_fourcc(*'XVID'), 
                                fps, 
                                (frame_w, frame_h)) 
    ref,frame=video_reader.read()
    trfn=0
    carn=0
    refs=0
    lx=light_Pos[0][0]*2.4
    ly=(light_Pos[0][1]-26)*2.16
    lrx=lx*2.4+30
    rrx=lx*2.4-30
    sy=(light_Pos[1][1]-26)*2.16
    slx=light_Pos[1][0]*2.4
    srx=light_Pos[2][0]*2.4

    print(lx, ly)
    carnums=0
    carlist=[]
    carlistnums=0
    run_a_red_light=0
    totalcarn=0
    print("fps",fps)

    totalcarn_list=[]
    carlistnums_list=[]
    while(ref):
        # 读取某一帧
        # 格式转变，BGRtoRGB
        refs=refs+1
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        font = ImageFont.truetype('font/simhei.ttf',28)
        if fps>27:
        # 进行检测
            if (refs-1)%10==0:
                # 转变成Image
                frame = Image.fromarray(np.uint8(frame))
                r_image,i,m,n,carlistnums,run_a_red_light,totalcarn= yolo.detect_image(frame,trfn,carn,lrx,rrx,carnums,carlist,sy, slx, srx,lx,ly)
                trfn=i
                carn=m
                carnums=n
                frame = np.array(r_image)
                #frame = np.array(yolo.detect_image(frame))

                # RGBtoBGR满足opencv显示格式
                frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
                video_writer.write(frame)
                
            else:
                frame = Image.fromarray(np.uint8(frame))

                draw = ImageDraw.Draw(frame)
                draw.rectangle(
                    (1300,150,1900,200),
                    fill="white")
                draw.text((1300,160,1900,180), "路口通过car的数量为:"+str(carlistnums), fill="black",font=font) 

                draw.rectangle(
                    (1300,50,1900,140),
                    fill="white")
                if totalcarn>=10:
                    draw.text((1300,60,1900,100), "当前路口机动车数量为"+str(totalcarn)+"大于9"+"  拥堵",font=font) 
                else:
                    draw.text((1300,60,1900,100), "当前路口机动车数量："+str(totalcarn), fill="black",font=font) 
                draw.text((1300,100,1800,140), "当前路口闯红灯数量："+str(run_a_red_light), fill="black",font=font)

                del draw
                frame = np.array(frame)
                frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
                video_writer.write(frame)

            if (refs-1)%600==0:
                totalcarn_list.append(totalcarn)
                carlistnums_list.append(carlistnums)
        
        else:
            if (refs-1)%5==0:
                frame = Image.fromarray(np.uint8(frame))
                r_image,i,m,n,carlistnums,run_a_red_light,totalcarn= yolo.detect_image(frame,trfn,carn,lrx,rrx,carnums,carlist,sy, slx, srx,lx,ly)
                trfn=i
                carn=m
                carnums=n
                frame = np.array(r_image)
                frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
                video_writer.write(frame)
            else:
                frame = Image.fromarray(np.uint8(frame))
                draw = ImageDraw.Draw(frame)
                draw.rectangle(
                    (1300,150,1900,200),
                    fill="white")
                draw.text((1300,160,1900,180), "路口通过car的数量为:"+str(carlistnums), fill="black",font=font) 

                draw.rectangle(
                    (1300,50,1900,140),
                    fill="white")
                if totalcarn>=10:
                    draw.text((1300,60,1900,100), "当前路口机动车数量为"+str(totalcarn)+"大于9"+"  拥堵",font=font) 
                else:
                    draw.text((1300,60,1900,100), "当前路口机动车数量："+str(totalcarn), fill="black",font=font) 
                draw.text((1300,100,1800,140), "当前路口闯红灯数量："+str(run_a_red_light), fill="black",font=font)

                del draw
                frame = np.array(frame)
                frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
                video_writer.write(frame)
            if (refs-1)%50==0:
                print(refs)
                totalcarn_list.append(totalcarn)
                carlistnums_list.append(carlistnums)

        ref,frame=video_reader.read()
    
    plt.rcParams['font.sans-serif'] = ['SimHei']
    if fps>27:
        X=[str(ni*20)+"s" for ni in range(1,len(totalcarn_list)+1)]
    else:
        X=[str(ni*2)+"s" for ni in range(1,len(totalcarn_list)+1)]


    plt.figure(figsize=(15,7))
    plt.plot(X,totalcarn_list,label='当前路口机动车数量')
    plt.plot(X,carlistnums_list,label='路口通过car数量')
    # 对应x轴与字符串
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.legend(fontsize=30)
    plt.xlabel('时间',fontsize=20)
    plt.ylabel('数量',fontsize=30)
    plt.title("路口车辆情况统计图",fontsize=30)
    plt.savefig(infomation_path())
   

    video_reader.release()
    video_writer.release()
    yolo.close_session()
    keras.backend.clear_session()
    
    
   

