# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\DeepLearning\mytraffic_cv\gui\InfoOut_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Infoout_Dialog(object):
    def setupUi(self, Infoout_Dialog):
        Infoout_Dialog.setObjectName("Infoout_Dialog")
        Infoout_Dialog.resize(382, 72)
        Infoout_Dialog.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Infoout_Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Infoout_Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Infoout_Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Out = QtWidgets.QPushButton(Infoout_Dialog)
        self.Out.setObjectName("Out")
        self.verticalLayout.addWidget(self.Out, 0, QtCore.Qt.AlignHCenter)
        self.Quit = QtWidgets.QPushButton(Infoout_Dialog)
        self.Quit.setObjectName("Quit")
        self.verticalLayout.addWidget(self.Quit, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 2, 1)
        self.comboBox = QtWidgets.QComboBox(Infoout_Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.retranslateUi(Infoout_Dialog)
        self.Quit.clicked.connect(Infoout_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Infoout_Dialog)

    def retranslateUi(self, Infoout_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Infoout_Dialog.setWindowTitle(_translate("Infoout_Dialog", "导出违法信息"))
        self.label.setText(_translate("Infoout_Dialog", "请选择导出类型："))
        self.Out.setText(_translate("Infoout_Dialog", "导出"))
        self.Quit.setText(_translate("Infoout_Dialog", "关闭"))

