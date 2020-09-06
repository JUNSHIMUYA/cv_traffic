import sys

from PyQt5 import  QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import *

from gui.Ui_Main import Ui_MainWindow  #导入创建的GUI类
from VedioDisplay import Display
from gui.Ui_InfoOut_Dialog import Ui_Infoout_Dialog
from gui.InfoOut import InfoOut
from gui.Ui_illegal_dialog import Ui_dialogillgal
from gui.imgOut import imgOut
from gui.Ui_help import Ui_Dialog

#自己建一个mywindows类，mywindow是自己的类名。QtWidgets.QMainWindow：继承该类方法
class Info_outWindow(QDialog):
    """信息导出窗口"""
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Infoout_Dialog()
        self.ui.setupUi(self)
        
        
class illegal_dialog(QDialog):
    """违章帧查看窗口"""
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_dialogillgal()
        self.ui.setupUi(self)


class mywindow(QtWidgets.QMainWindow):
    """主窗口"""
    def __init__(self):
        #继承自多个父类的子类初始化
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.DisplayLabel.setMouseTracking(True)
        self.ui.Button_GetPos.clicked.connect(self.Get_Pos)
        self.checkstat = False
        #初始化按钮
        self.ui.Open.setEnabled(False)
        self.ui.Button_imgout.setEnabled(False)
        self.ui.Button_infoout.setEnabled(False)

    def mousePressEvent(self, event):
        if self.checkstat is True:
            pos = event.x(),event.y()
            self.pos_list.append(pos)
            print(self.pos_list)
            if (len(self.pos_list)==1):
                dig = QMessageBox.information(self, "提示", "直行红绿灯坐标参数获取成功！", QMessageBox.Yes)
            elif (len(self.pos_list)==2):
                dig = QMessageBox.information(self, "提示", "直行车道停车线左坐标参数获取成功！", QMessageBox.Yes)
            elif (len(self.pos_list)==3):
                dig = QMessageBox.information(self, "提示", "直行车道停车线右坐标参数获取成功！\n\n参数获取结束", QMessageBox.Yes)
                self.checkstat = False
                self.ui.Api_button.setEnabled(True)
            else:
                dig = QMessageBox.warning(self, "警告", "获取坐标参数过多！", QMessageBox.Yes)
                self.pos_list.pop()


    def Get_Pos(self):
        self.pos_list=[]
        self.checkstat = True
        dig = QMessageBox.information(self, "提示", "请按顺序点击路口对应的点位：\n" + "1、路口的直行红绿灯坐标。\n\n" + "2、路口中的直行车道停车线左坐标。\n\n" + "3、路口中的直行车道停车线右坐标。", QMessageBox.Yes)



# QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。
# 对于GUI程序必须至少有一个这样的实例来让程序运行。
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    #主窗口和子窗口关联以及初始化
    mainWnd = mywindow()
    InfooutWindow = Info_outWindow()
    illegalDialog = illegal_dialog()
    
    mainWnd.ui.Button_infoout.clicked.connect(InfooutWindow.show)
    mainWnd.ui.Button_imgout.clicked.connect(illegalDialog.show)
    
    #主、子窗口的功能实现类
    display = Display(mainWnd)
    infoout = InfoOut(InfooutWindow)
    imgout = imgOut(illegalDialog)

    mainWnd.show()#有了实例，就得让它显示，show()是QWidget的方法，用于显示窗口。

    sys.exit(app.exec_())

