from time import ctime, sleep
import time
from typing import Optional, Pattern, Tuple
import cv2
import os
import threading

from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QHeaderView, QDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtGui import  QStandardItemModel,QStandardItem

import gui.PATH as PATH
from myvideo import detect2
from gui.Ui_help import Ui_Dialog
from gui.Ui_RoadChoose import Ui_Dialog_chooseRoad
from gui.Ui_SetRoad import Ui_SetRoad_dialog


class helpdialog(QDialog):
    """帮助手册子菜单实现类"""
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class SetRoad_dialog(QDialog):
    """帮助手册子菜单实现类"""
    def __init__(self, mainWnd):
        QDialog.__init__(self)
        self.ui = Ui_SetRoad_dialog()
        self.ui.setupUi(self)
        self.mainWnd = mainWnd
        self.ui.Box_Existed_Roads.addItems(PATH.get_allroads())
        self.ui.Box_Existed_Roads.setCurrentIndex(-1)
        self.ui.pushButton_ok.clicked.connect(self.set_road)
    
    def set_road(self):
        """路口设置对话框响应函数"""
        self.mainWnd.ui.Open.setEnabled(True)
        self.mainWnd.ui.Button_imgout.setEnabled(True)
        self.mainWnd.ui.Button_infoout.setEnabled(True)
        if self.ui.Text_NewRoad.toPlainText() is '' and self.ui.Box_Existed_Roads.currentIndex() is not -1:
            PATH.setValue('RoadName', self.ui.Box_Existed_Roads.currentText())
            self.mainWnd.ui.label_road_text.setText(self.ui.Box_Existed_Roads.currentText())
        elif self.ui.Text_NewRoad.toPlainText() is not '':
            PATH.setValue('RoadName', self.ui.Text_NewRoad.toPlainText())
            self.mainWnd.ui.label_road_text.setText(self.ui.Text_NewRoad.toPlainText())
        else:
            dig = QMessageBox.warning(self, "警告", "当前未设置路口！", QMessageBox.Yes)
            return
        dig = QMessageBox.information(self, "提示", "路口设置成功", QMessageBox.Yes)
        self.mainWnd.ui.Open.setEnabled(True)
        self.mainWnd.ui.Button_imgout.setEnabled(True)
        self.mainWnd.ui.Button_infoout.setEnabled(True)


class roadchoosedialog(QDialog):
    """选择已处理视频对话框"""
    show_processed_info = pyqtSignal()
    def __init__(self, mainWnd):
        QDialog.__init__(self)
        self.ui = Ui_Dialog_chooseRoad()
        self.ui.setupUi(self)
        self.ui.chooseRoad.addItems(PATH.get_allroads())
        self.ui.chooseRoad.currentIndexChanged.connect(self.set_roadinfo)
        self.ui.pushButton_ok.clicked.connect(self.get_roadinfo)
        self.mainWnd = mainWnd
        self.ui.chooseRoad.setCurrentIndex(-1)

    def set_roadinfo(self):
        """搜索对应路口文件夹的违法记录"""
        self.ChosedRoad = self.ui.chooseRoad.currentText()
        if self.ui.chooseRoad.currentIndex() == -1:
            pass
        else:
            self.ui.choose_time.clear()
            VedioList = PATH.get_chosed_roadinfo(self.ChosedRoad)
            if len(VedioList) == 0:
                dig = QMessageBox.information(self, "提示", "当前路口没有处理视频！", QMessageBox.Yes)
            else:
                self.ui.choose_time.addItem('所有时间')
                self.ui.choose_time.addItems(VedioList)

    def get_roadinfo(self):
        """确定路口和时间段之后的操作"""
        if self.ui.chooseRoad.currentIndex() == -1:
            dig = QMessageBox.information(self, "提示", "未选择路口", QMessageBox.Yes)
            return
        self.ChosedTime = self.ui.choose_time.currentText()
        self.mainWnd.ui.label_road_text.setText(self.ChosedRoad)

        if self.ChosedTime == "所有时间" and self.ChosedRoad != "所有路口":
            PATH.setValue('RoadName', self.ChosedRoad)
            PATH.setValue('CVedioDate', self.ChosedTime)
            PATH.bool_alltimes = True
        else:
            PATH.bool_alltimes = False
            try:
                PATH.setValue('RoadName', self.ChosedRoad)
                PATH.setValue('CVedioDate', self.ChosedTime)
                Vedio_OutFileName = PATH.detect_result_path + self.ChosedRoad + '\\'+ self.ChosedTime+"\\"+"Vedio_out.avi"
                self.mainWnd.Vedioplayname = Vedio_OutFileName
                self.mainWnd.specialroad = True
                self.show_processed_info.emit()
            except:
                dig = QMessageBox.warning(self, "警告", "未找到目标视频文件", QMessageBox.Yes)
        self.mainWnd.ui.label_date_text.setText(self.ChosedTime)
        self.mainWnd.ui.Open.setEnabled(True)
        self.mainWnd.ui.Button_imgout.setEnabled(True)
        self.mainWnd.ui.Button_infoout.setEnabled(True)
        

class Worker(QObject):
    def __init__(self, in_name, out_name,light_Pos):
        super().__init__()
        self.fileName = in_name
        self.video_outname = out_name
        self.light_Pos = light_Pos
        

    finished = pyqtSignal()
    show_processed_vedio = pyqtSignal()

    @pyqtSlot()
    def work(self): # A slot takes no params
        print("检测开始")
        detect2(self.fileName,self.video_outname,self.light_Pos)
        self.finished.emit()
        self.show_processed_vedio.emit()
        print("检测结束")


class Display:
    def __init__(self, mainWnd):
        self.mainWnd = mainWnd
        self.ui = mainWnd.ui
        self.stop = False
        self.specialroad = False
        self.fileName = ''
        self.Vedioplayname = ''
        
        #界面所有按钮和label的初始化
        self.ui.Open.setEnabled(True)
        self.ui.Close.setEnabled(False)
        self.ui.Api_button.setEnabled(False)
        self.ui.Continue.setEnabled(False)
        self.ui.Button_GetPos.setEnabled(False)
        self.model = QStandardItemModel()#存储任意结构数据
        self.model.setHorizontalHeaderLabels(['车牌号码','违章类型'])
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.setModel(self.model)

        # 信号槽设置
        self.ui.Open.clicked.connect(self.Open)
        self.ui.Close.clicked.connect(self.Close)
        self.ui.Continue.clicked.connect(self.Stop)
        self.ui.Api_button.clicked.connect(self.Api_button)

        #菜单栏设置
        self.ui.delete_cache.triggered.connect(self.Delet_cache_data)
        self.ui.actionHelp.triggered.connect(self.helpdig)
        self.ui.action_SetRoad.triggered.connect(self.set_road)
        self.ui.action_choose_road.triggered.connect(self.choose_road)
        

        # 创建一个关闭事件并设为未触发
        self.stopEvent = threading.Event()
        self.stopEvent.clear()

        #创建用于运行detect的线程
        self.thread = QThread()  # no parent!


    def Open(self):
        """打开视频原文件按钮响应函数"""
        self.fileName, self.fileType = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.avi')
        if self.fileName is None or '.avi' not in self.fileName:
            return
        elif 'out' not in self.fileName: 
            VedioDate = time.ctime(os.path.getctime(self.fileName))
            VedioDate = VedioDate.replace(' ', "_").replace(':', '_').replace('__', '_')
            PATH.setValue('CVedioDate', VedioDate)
            self.ui.label_date_text.setText(PATH.get_VedioDate())
            self.video_outname = PATH.run_a_red_light_vedio_path() 

        #刷新信息显示
        self.ui.label_roadinfo.setText("                   车流量信息展示区域")
        self.model = QStandardItemModel()#存储任意结构数据
        self.model.setHorizontalHeaderLabels(['车牌号码','违章类型'])
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableView.setModel(self.model)

        # 创建视频显示线程
        self.Vedioplayname = self.fileName
        th = threading.Thread(target=self.Display)
        th.start()
        
        
    def Stop(self):
        """暂停按钮响应函数"""
        self.stop = not self.stop
        self.mainWnd.checkstat = False

    def Close(self):
        """关闭按钮响应函数"""
        # 关闭事件设为触发，关闭视频播放
        self.ui.Close.setEnabled(False)
        self.ui.Api_button.setEnabled(False)
        self.ui.Continue.setEnabled(False)
        self.ui.Button_GetPos.setEnabled(False)
        self.stopEvent.set()
        sleep(0.1)
        self.thread.quit()

    def Display(self):
        """视频展示函数"""
        print(self.Vedioplayname)
        self.specialroad = False
        self.cap = cv2.VideoCapture(self.Vedioplayname)
        self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)

        self.ui.Open.setEnabled(False)
        self.ui.Close.setEnabled(True)
        self.ui.Continue.setEnabled(True)
        self.ui.Button_GetPos.setEnabled(True)
    
        while self.cap.isOpened():
            if not self.mainWnd.checkstat and not self.stop:
                success,frame=self.cap.read()
                # RGB转BGR
                try:
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                    img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    self.ui.DisplayLabel.setPixmap(QPixmap.fromImage(img))
                    self.ui.DisplayLabel.setScaledContents(True)
                    cv2.waitKey(int(1000 / self.frameRate))
                except:
                    self.stopEvent.set()
            
            # 判断关闭事件是否已触发
            if self.stopEvent.is_set():
                # 关闭事件置为未触发，清空显示label
                self.stopEvent.clear()
                self.ui.DisplayLabel.clear()
                self.ui.Close.setEnabled(False)
                self.ui.Open.setEnabled(True)
                break
        self.stopEvent.set()
        self.stopEvent.clear()
        self.ui.Close.setEnabled(False)
        self.ui.Open.setEnabled(True)
        self.cap.release() #关闭打开的视频
        print("视频播放线程结束")


    def Api_button(self):
        """检测API接口"""
        try:
            print(self.fileName)
            print(self.video_outname)
            PATH.cheackFolders()
            
            self.Pos_list = self.mainWnd.pos_list
            self.worker = Worker(self.fileName, self.video_outname, self.Pos_list)
            self.worker.finished.connect(self.thread.quit)
            self.thread.started.connect(self.worker.work)
            self.worker.show_processed_vedio.connect(self.show_processed_vedio)

            self.stopEvent.set()
            print("正在关原视频")
            sleep(1)
            self.ui.DisplayLabel.setText( " "*30 +"正在检测视频，请勿退出系统")
            print("Qthread开始")
            self.worker.moveToThread(self.thread)
            self.thread.start()
        except:
            dig = QMessageBox.warning(self.mainWnd, "警告", "错误操作！可选择再次打开程序", QMessageBox.Yes)


    def show_processed_vedio(self):
        """显示detected视频以及违法信息"""
        #违章表格初始化
        
        with open(PATH.run_a_red_lightpath(), 'r', encoding='UTF-8') as fp:
            data =[]
            data = fp.readlines()
            if '\n' in data:
                data.remove('\n')
            row_lenth = len(data)
        self.ui.label_roadinfo.setPixmap(QPixmap(PATH.infomation_path()))
        self.ui.label_roadinfo.setScaledContents(True)
        self.model = QStandardItemModel()#存储任意结构数据
        self.model.setHorizontalHeaderLabels(['车牌号码','违章类型'])
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row in range(row_lenth):
            plate_number, ilegal_type = data[row].split(' ')   
            ilegal_type = ilegal_type.replace('\n','')
            i = QStandardItem(plate_number)
            j = QStandardItem(ilegal_type)
            self.model.setItem(row,0,i)
            self.model.setItem(row,1,j)
        self.ui.tableView.setModel(self.model)

        # 创建视频显示线程
        if self.specialroad is not True:
            self.Vedioplayname = self.video_outname
        self.th1 = threading.Thread(target=self.Display)
        self.th1.start()


    def Delet_cache_data(self):
        """删除缓存数据"""
        res1 = QMessageBox.warning(self.mainWnd, "警告", "请确保已保存好了必要的信息，确定继续吗？", QMessageBox.Yes | QMessageBox.No)
        if (QMessageBox.No == res1):
            return
        try:
            with open(PATH.resultpath, "w", encoding='UTF-8') as fp:
                pass
            img_path = [PATH.caroutputpath, PATH.caridpath, PATH.trafficoutputpath]
            for i in range(0,3):
                os.chdir(img_path[i])
                fileList = list(os.listdir()) 
                for file in fileList: 
                    os.remove(file) 
        except PermissionError:
            res2 = QMessageBox.information(self.mainWnd, "提示", "您正在使用该文件，请关闭后再执行", QMessageBox.Yes)
            return

        print("delete successfully")
        res2 = QMessageBox.information(self.mainWnd, "提示", "删除缓存成功！", QMessageBox.Yes)


    def helpdig(self):
        """显示帮助文档"""
        self.hlpdig = helpdialog()
        self.hlpdig.show()
        

    def set_road(self):
        """路口名称设置"""
        PATH.bool_alltimes = False
        PATH.bool_allroads = False
        self.SetRoad_Dig = SetRoad_dialog(self)
        self.SetRoad_Dig.show()
        

    def choose_road(self):
        """选择已经处理的视频"""
        self.choosedig = roadchoosedialog(self)
        self.choosedig.show()
        self.choosedig.show_processed_info.connect(self.show_processed_vedio)