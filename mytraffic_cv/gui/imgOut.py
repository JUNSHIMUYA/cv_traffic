import sys, os 
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox,QDialog

import gui.PATH as PATH
from gui.Ui_ChangeInfo import Ui_Dialog_ChangeInfo


class ChangeInfo_Dialog(QDialog):
    def __init__(self, DisplayObject):
        QDialog.__init__(self)
        self.ui = Ui_Dialog_ChangeInfo()
        self.ui.setupUi(self)
        self.DisplayObject = DisplayObject
        self.ui.pushButton_ok.clicked.connect(self.Change)

    def Change(self):
        """纠正信息按钮响应函数"""
        try:
            img_dirpath = self.DisplayObject.current_img_dirpath
            self.ChangePlate = self.DisplayObject.ui.plate_number.text()
            self.ChangeType = self.DisplayObject.ui.illegal_type.text()
            oldnumber = self.ChangePlate
            oldtype = self.ChangeType
            oldname = img_dirpath + self.ChangePlate +'_'+  self.ChangeType + ".jpg"
            print(oldname)

            #更新img文件
            if self.ui.textEdit_ChangePlate.toPlainText() is not '' and self.ui.textEdit_ChangeType.toPlainText() is not '':
                self.ChangePlate = self.ui.textEdit_ChangePlate.toPlainText()
                self.ChangeType = self.ui.textEdit_ChangeType.toPlainText()
            elif self.ui.textEdit_ChangePlate.toPlainText() is not '' and self.ui.textEdit_ChangeType.toPlainText() is '':
                 self.ChangePlate = self.ui.textEdit_ChangePlate.toPlainText()
            elif self.ui.textEdit_ChangePlate.toPlainText() is '' and self.ui.textEdit_ChangeType.toPlainText() is not '':
                self.ChangeType = self.ui.textEdit_ChangeType.toPlainText()
            else:
                pass

            newname = img_dirpath + self.ChangePlate +'_'+  self.ChangeType + ".jpg"
            print(newname)
            os.rename(oldname, newname)

            #更新txt文件
            txtpath = os.path.dirname(os.path.dirname(img_dirpath))+ '\\illegal_car_info.txt'
            with open(txtpath, 'r', encoding='UTF-8') as fp:
                lines = fp.readlines()
                for i in range(len(lines)):
                    if oldnumber and oldtype in lines[i]:
                        lines[i] = self.ChangePlate +" "+ self.ChangeType + "\n"
                fp.close()
            with open(txtpath, 'w', encoding='UTF-8') as fp:
                fp.writelines(lines)
            self.DisplayObject.img_init()
            self.DisplayObject.next_img()
            box = QMessageBox.warning(self, "提示", "修改成功！", QMessageBox.Yes)
        except:
            box = QMessageBox.warning(self, "提示", "修改失败", QMessageBox.Yes)



class imgOut:
    def __init__(self, wnd):
        self.ui = wnd.ui
        self.wnd = wnd
        self.current_img_index = 0
        self.imgnames_list = []
        self.date_allroads_list = []
        self.ui.before.setEnabled(False)
        self.ui.delete_info.setEnabled(False)
        self.ui.ChangeButton.setEnabled(False)

        self.ui.before.clicked.connect(self.before_img)
        self.ui.next.clicked.connect(self.next_img)
        self.ui.delete_info.clicked.connect(self.delet_info)
        self.ui.ChangeButton.clicked.connect(self.change_info)

    def img_init(self):
        """初始化img列表"""
        if PATH.bool_alltimes is True:
            self.imgpaths = []
            self.imgs_dict = PATH.get_road_imgspaths(PATH.get_roadname())
            for img_info in self.imgs_dict.keys():
                Road, Date, img = img_info.split(':')
                self.imgnames_list.append(img)
                self.date_allroads_list.append(Date)
                self.imgpaths.append(self.imgs_dict[img_info])
        else:
            self.imgnames_list = list(os.listdir(PATH.run_a_red_light_img_path()))
        
        if len(self.imgnames_list) != 0:
            self.display_info()
            self.ui.before.setEnabled(True)
            self.ui.delete_info.setEnabled(True)
            self.ui.ChangeButton.setEnabled(True)
        else:
            box = QMessageBox.warning(self.wnd, "提示", "库存为空", QMessageBox.Yes)


    def before_img(self):
        """上一张图片"""
        if self.current_img_index == 0:
            return
        else:
            self.current_img_index = self.current_img_index - 1
        self.display_info()
        

    def next_img(self):
        """下一张图片"""
        if len(self.imgnames_list) == 0:
            self.img_init()
        else:
            self.ui.before.setEnabled(True)
            self.ui.delete_info.setEnabled(True)
            self.ui.ChangeButton.setEnabled(True)
            if self.current_img_index == len(self.imgnames_list)-1:
                self.current_img_index = 0
            else:
                self.current_img_index = self.current_img_index + 1
            self.display_info()


    def display_info(self):
        """展示违法信息"""
        try:
            n, m = self.imgnames_list[self.current_img_index].split('_')
            m = str(m).replace('.jpg', '')
            self.ui.plate_number.setText(n)
            self.ui.illegal_type.setText(m)
            if PATH.bool_alltimes is True:
                Date = self.date_allroads_list[self.current_img_index]
                RoadName = PATH.get_roadname()
                self.current_img_dirpath = PATH.detect_result_path + RoadName + "\\" + Date +  "\\illegal_imgs\\"
                self.ui.label_Road_Belong.setText(RoadName)
                self.ui.label_Time_Belong.setText(Date)
                self.ui.label.setPixmap(QPixmap(self.imgpaths[self.current_img_index]))
            else:
                self.current_img_dirpath = PATH.run_a_red_light_img_path()
                self.ui.label_Road_Belong.setText(PATH.get_roadname())
                self.ui.label_Time_Belong.setText(PATH.get_VedioDate())
                self.ui.label.setPixmap(QPixmap(PATH.run_a_red_light_img_path() + self.imgnames_list[self.current_img_index]))
            self.ui.label.setScaledContents(True)
        except:
            box = QMessageBox.warning(self.wnd, "提示", "库存为空", QMessageBox.Yes)


    def delet_info(self):
        """删除展示车辆的违法信息"""
        box = QMessageBox.warning(self.wnd, "提示", "确定删除该车辆的违法信息？", QMessageBox.Yes | QMessageBox.No)
        if box == QMessageBox.No:
            return
        else:
            try:
                del_name_path = self.imgnames_list.pop(self.current_img_index)
                del_name = del_name_path[0:7]
                if PATH.bool_alltimes is True:  
                    os.remove(self.imgpaths[self.current_img_index])
                    _ = self.imgpaths[self.current_img_index].split("\\")
                    txtpath = PATH.Road_ROOTpath() + _[4] + "\\illegal_car_info.txt"
                else:
                    os.remove(PATH.run_a_red_light_img_path() + del_name_path)
                    txtpath = PATH.run_a_red_lightpath()

                with open(txtpath, 'r', encoding='UTF-8') as fp:
                    lines = fp.readlines()
                    for i in range(len(lines)):
                        if del_name in lines[i]:
                            lines[i] = ''
                    fp.close()
                with open(txtpath, 'w', encoding='UTF-8') as fp:
                    fp.writelines(lines)
                box = QMessageBox.warning(self.wnd, "提示", "删除成功！", QMessageBox.Yes)
            except:
                box = QMessageBox.warning(self.wnd, "提示", "删除错误", QMessageBox.Yes)
            self.current_img_index = 0
            self.display_info()

        
    def change_info(self):
        self.ChangeInfo = ChangeInfo_Dialog(self)
        self.ChangeInfo.show()