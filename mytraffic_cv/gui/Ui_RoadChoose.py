# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\YoloProject\mytraffic_cv\gui\RoadChoose.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_chooseRoad(object):
    def setupUi(self, Dialog_chooseRoad):
        Dialog_chooseRoad.setObjectName("Dialog_chooseRoad")
        Dialog_chooseRoad.resize(369, 209)
        Dialog_chooseRoad.setMinimumSize(QtCore.QSize(0, 0))
        Dialog_chooseRoad.setMaximumSize(QtCore.QSize(1000000, 10000000))
        self.pushButton_ok = QtWidgets.QPushButton(Dialog_chooseRoad)
        self.pushButton_ok.setGeometry(QtCore.QRect(160, 160, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_quit = QtWidgets.QPushButton(Dialog_chooseRoad)
        self.pushButton_quit.setGeometry(QtCore.QRect(260, 160, 93, 28))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.chooseRoad = QtWidgets.QComboBox(Dialog_chooseRoad)
        self.chooseRoad.setGeometry(QtCore.QRect(20, 38, 331, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.chooseRoad.setFont(font)
        self.chooseRoad.setObjectName("chooseRoad")
        self.label_2 = QtWidgets.QLabel(Dialog_chooseRoad)
        self.label_2.setGeometry(QtCore.QRect(20, -2, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog_chooseRoad)
        self.label.setGeometry(QtCore.QRect(19, 73, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.choose_time = QtWidgets.QComboBox(Dialog_chooseRoad)
        self.choose_time.setGeometry(QtCore.QRect(20, 110, 331, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.choose_time.setFont(font)
        self.choose_time.setObjectName("choose_time")

        self.retranslateUi(Dialog_chooseRoad)
        self.pushButton_quit.clicked.connect(Dialog_chooseRoad.close)
        self.pushButton_ok.clicked.connect(Dialog_chooseRoad.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog_chooseRoad)

    def retranslateUi(self, Dialog_chooseRoad):
        _translate = QtCore.QCoreApplication.translate
        Dialog_chooseRoad.setWindowTitle(_translate("Dialog_chooseRoad", "查看已处理视频"))
        self.pushButton_ok.setText(_translate("Dialog_chooseRoad", "确定"))
        self.pushButton_quit.setText(_translate("Dialog_chooseRoad", "取消"))
        self.label_2.setText(_translate("Dialog_chooseRoad", "请选择路口："))
        self.label.setText(_translate("Dialog_chooseRoad", "请选择时间段："))

