# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'del_student.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form_del(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 612)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 150, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 310, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 300, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 430, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 430, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.shanchu)
        self.pushButton_2.clicked.connect(self.close)

    def shanchu(self):
        num1=self.lineEdit.text()
        db=pymysql.connect('localhost', 'root', '285300', 'student')
        cur=db.cursor()
        sql = "delete from info where (num = '%s');"%num1
        t=(cur.execute(sql))
        print(t)
        db.commit()
        if t==1:
            mbox=QtWidgets.QMessageBox
            mbox.question(self,"标题","删除成功",mbox.Ok)
        else:
            mbox = QtWidgets.QMessageBox
            mbox.question(self, "标题", "删除失败", mbox.Ok)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学生信息管理系统"))
        self.label.setText(_translate("Form", "删除学生信息"))
        self.label_2.setText(_translate("Form", "待删除学号："))
        self.pushButton.setText(_translate("Form", "确认删除"))
        self.pushButton_2.setText(_translate("Form", "返回首页"))
