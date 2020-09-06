# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\YoloProject\mytraffic_cv\gui\ChangeInfo.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_ChangeInfo(object):
    def setupUi(self, Dialog_ChangeInfo):
        Dialog_ChangeInfo.setObjectName("Dialog_ChangeInfo")
        Dialog_ChangeInfo.resize(393, 265)
        self.pushButton_quit = QtWidgets.QPushButton(Dialog_ChangeInfo)
        self.pushButton_quit.setGeometry(QtCore.QRect(280, 210, 91, 31))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_ok = QtWidgets.QPushButton(Dialog_ChangeInfo)
        self.pushButton_ok.setGeometry(QtCore.QRect(170, 210, 91, 31))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.label = QtWidgets.QLabel(Dialog_ChangeInfo)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_ChangeInfo)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_ChangePlate = QtWidgets.QTextEdit(Dialog_ChangeInfo)
        self.textEdit_ChangePlate.setGeometry(QtCore.QRect(10, 50, 371, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.textEdit_ChangePlate.setFont(font)
        self.textEdit_ChangePlate.setObjectName("textEdit_ChangePlate")
        self.textEdit_ChangeType = QtWidgets.QTextEdit(Dialog_ChangeInfo)
        self.textEdit_ChangeType.setGeometry(QtCore.QRect(10, 160, 371, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.textEdit_ChangeType.setFont(font)
        self.textEdit_ChangeType.setObjectName("textEdit_ChangeType")
        self.line = QtWidgets.QFrame(Dialog_ChangeInfo)
        self.line.setGeometry(QtCore.QRect(0, 100, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog_ChangeInfo)
        self.pushButton_ok.clicked.connect(Dialog_ChangeInfo.accept)
        self.pushButton_quit.clicked.connect(Dialog_ChangeInfo.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_ChangeInfo)

    def retranslateUi(self, Dialog_ChangeInfo):
        _translate = QtCore.QCoreApplication.translate
        Dialog_ChangeInfo.setWindowTitle(_translate("Dialog_ChangeInfo", "纠正违章信息"))
        self.pushButton_quit.setText(_translate("Dialog_ChangeInfo", "取消"))
        self.pushButton_ok.setText(_translate("Dialog_ChangeInfo", "确定"))
        self.label.setText(_translate("Dialog_ChangeInfo", "纠正车牌号为："))
        self.label_2.setText(_translate("Dialog_ChangeInfo", "纠正违法类型为："))

