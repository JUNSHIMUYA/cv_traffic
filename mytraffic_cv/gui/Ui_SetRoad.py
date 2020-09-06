# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\YoloProject\mytraffic_cv\gui\SetRoad.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetRoad_dialog(object):
    def setupUi(self, SetRoad_dialog):
        SetRoad_dialog.setObjectName("SetRoad_dialog")
        SetRoad_dialog.resize(397, 255)
        self.pushButton_ok = QtWidgets.QPushButton(SetRoad_dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(190, 210, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_quit = QtWidgets.QPushButton(SetRoad_dialog)
        self.pushButton_quit.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.label = QtWidgets.QLabel(SetRoad_dialog)
        self.label.setGeometry(QtCore.QRect(20, 120, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Text_NewRoad = QtWidgets.QTextEdit(SetRoad_dialog)
        self.Text_NewRoad.setGeometry(QtCore.QRect(20, 160, 361, 31))
        self.Text_NewRoad.setObjectName("Text_NewRoad")
        self.Box_Existed_Roads = QtWidgets.QComboBox(SetRoad_dialog)
        self.Box_Existed_Roads.setGeometry(QtCore.QRect(20, 40, 361, 31))
        self.Box_Existed_Roads.setObjectName("Box_Existed_Roads")
        self.label_2 = QtWidgets.QLabel(SetRoad_dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SetRoad_dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(SetRoad_dialog)
        self.pushButton_ok.clicked.connect(SetRoad_dialog.accept)
        self.pushButton_quit.clicked.connect(SetRoad_dialog.close)
        QtCore.QMetaObject.connectSlotsByName(SetRoad_dialog)

    def retranslateUi(self, SetRoad_dialog):
        _translate = QtCore.QCoreApplication.translate
        SetRoad_dialog.setWindowTitle(_translate("SetRoad_dialog", "设置路口对话框"))
        self.pushButton_ok.setText(_translate("SetRoad_dialog", "确定"))
        self.pushButton_quit.setText(_translate("SetRoad_dialog", "取消"))
        self.label.setText(_translate("SetRoad_dialog", "设置新的路口名："))
        self.label_2.setText(_translate("SetRoad_dialog", "选择已有路口名："))
        self.label_3.setText(_translate("SetRoad_dialog", "或者"))

