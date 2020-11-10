# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登录-注册界面.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_main(object):
    def setupUi(self, Form_main):
        Form_main.setObjectName("Form_main")
        Form_main.resize(633, 514)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Form_main.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Form_main)
        self.pushButton.setGeometry(QtCore.QRect(140, 120, 371, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form_main)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 260, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form_main)
        QtCore.QMetaObject.connectSlotsByName(Form_main)

    def retranslateUi(self, Form_main):
        _translate = QtCore.QCoreApplication.translate
        Form_main.setWindowTitle(_translate("Form_main", "登录-注册界面"))
        self.pushButton.setText(_translate("Form_main", "用户登录"))
        self.pushButton_2.setText(_translate("Form_main", "用户注册"))
