# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\mytraffic_cv\gui\illegal_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogillgal(object):
    def setupUi(self, dialogillgal):
        dialogillgal.setObjectName("dialogillgal")
        dialogillgal.resize(891, 580)
        dialogillgal.setMinimumSize(QtCore.QSize(891, 580))
        dialogillgal.setMaximumSize(QtCore.QSize(891, 580))
        self.line = QtWidgets.QFrame(dialogillgal)
        self.line.setGeometry(QtCore.QRect(660, 0, 41, 581))
        self.line.setMaximumSize(QtCore.QSize(41, 581))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(dialogillgal)
        self.label_2.setGeometry(QtCore.QRect(690, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plate_number = QtWidgets.QLabel(dialogillgal)
        self.plate_number.setGeometry(QtCore.QRect(690, 30, 201, 21))
        self.plate_number.setText("")
        self.plate_number.setObjectName("plate_number")
        self.label_4 = QtWidgets.QLabel(dialogillgal)
        self.label_4.setGeometry(QtCore.QRect(690, 60, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.illegal_type = QtWidgets.QLabel(dialogillgal)
        self.illegal_type.setGeometry(QtCore.QRect(690, 90, 191, 21))
        self.illegal_type.setText("")
        self.illegal_type.setObjectName("illegal_type")
        self.before = QtWidgets.QPushButton(dialogillgal)
        self.before.setGeometry(QtCore.QRect(730, 270, 101, 51))
        self.before.setObjectName("before")
        self.next = QtWidgets.QPushButton(dialogillgal)
        self.next.setGeometry(QtCore.QRect(730, 350, 101, 51))
        self.next.setObjectName("next")
        self.line_2 = QtWidgets.QFrame(dialogillgal)
        self.line_2.setGeometry(QtCore.QRect(680, 50, 211, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(dialogillgal)
        self.line_3.setGeometry(QtCore.QRect(680, 110, 211, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.delete_info = QtWidgets.QPushButton(dialogillgal)
        self.delete_info.setGeometry(QtCore.QRect(730, 510, 101, 51))
        self.delete_info.setObjectName("delete_info")
        self.ChangeButton = QtWidgets.QPushButton(dialogillgal)
        self.ChangeButton.setGeometry(QtCore.QRect(730, 430, 101, 51))
        self.ChangeButton.setObjectName("ChangeButton")
        self.label_3 = QtWidgets.QLabel(dialogillgal)
        self.label_3.setGeometry(QtCore.QRect(690, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_4 = QtWidgets.QFrame(dialogillgal)
        self.line_4.setGeometry(QtCore.QRect(680, 170, 211, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_5 = QtWidgets.QLabel(dialogillgal)
        self.label_5.setGeometry(QtCore.QRect(690, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line_5 = QtWidgets.QFrame(dialogillgal)
        self.line_5.setGeometry(QtCore.QRect(680, 230, 211, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_Road_Belong = QtWidgets.QLabel(dialogillgal)
        self.label_Road_Belong.setGeometry(QtCore.QRect(690, 150, 181, 21))
        self.label_Road_Belong.setText("")
        self.label_Road_Belong.setObjectName("label_Road_Belong")
        self.label_Time_Belong = QtWidgets.QLabel(dialogillgal)
        self.label_Time_Belong.setGeometry(QtCore.QRect(690, 210, 201, 21))
        self.label_Time_Belong.setText("")
        self.label_Time_Belong.setObjectName("label_Time_Belong")
        self.label = QtWidgets.QLabel(dialogillgal)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 581))
        self.label.setMinimumSize(QtCore.QSize(681, 581))
        self.label.setObjectName("label")

        self.retranslateUi(dialogillgal)
        QtCore.QMetaObject.connectSlotsByName(dialogillgal)

    def retranslateUi(self, dialogillgal):
        _translate = QtCore.QCoreApplication.translate
        dialogillgal.setWindowTitle(_translate("dialogillgal", "查看违法帧"))
        self.label_2.setText(_translate("dialogillgal", "车牌号码："))
        self.label_4.setText(_translate("dialogillgal", "违法类别："))
        self.before.setText(_translate("dialogillgal", "上一张"))
        self.next.setText(_translate("dialogillgal", "下一张"))
        self.delete_info.setText(_translate("dialogillgal", "删除信息"))
        self.ChangeButton.setText(_translate("dialogillgal", "纠正信息"))
        self.label_3.setText(_translate("dialogillgal", "所在路口："))
        self.label_5.setText(_translate("dialogillgal", "时间段："))
        self.label.setText(_translate("dialogillgal", "                                 点击下一张开始展示"))

