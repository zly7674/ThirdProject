# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_student.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form_add(object):
    def setupUi(self, Form_add):
        Form_add.setObjectName("Form_add")
        Form_add.resize(729, 664)
        self.label = QtWidgets.QLabel(Form_add)
        self.label.setGeometry(QtCore.QRect(270, 130, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_add)
        self.label_2.setGeometry(QtCore.QRect(210, 250, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_add)
        self.label_3.setGeometry(QtCore.QRect(211, 320, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form_add)
        self.label_4.setGeometry(QtCore.QRect(211, 380, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form_add)
        self.lineEdit.setGeometry(QtCore.QRect(300, 240, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form_add)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 310, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form_add)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 370, 221, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Form_add)
        self.pushButton.setGeometry(QtCore.QRect(230, 490, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form_add)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 490, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form_add)
        QtCore.QMetaObject.connectSlotsByName(Form_add)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.confirm)#确认添加函数

    def confirm(self):
        num=self.lineEdit.text()
        id=self.lineEdit_2.text()
        score=int(self.lineEdit_3.text())
        print(num,id,score)
        db = pymysql.connect('localhost', 'root', '285300', 'student')
        cur = db.cursor()
        sql = "insert into info values('%s','%s','%d');" % (num,id,score)
        try:
            cur.execute(sql)
            db.commit()
            mbox=QtWidgets.QMessageBox
            mbox.question(self,"标题","添加成功",mbox.Ok)
        except Exception as e:
            db.rollback()  # 失败回滚到操作之前的状态
            print("Faild:", e)
            mbox = QtWidgets.QMessageBox
            mbox.question(self, "标题", "添加失败", mbox.Ok)
            cur.close()
            db.close()


    def retranslateUi(self, Form_add):
        _translate = QtCore.QCoreApplication.translate
        Form_add.setWindowTitle(_translate("Form_add", "学生信息管理系统"))
        self.label.setText(_translate("Form_add", "添加学生信息"))
        self.label_2.setText(_translate("Form_add", "学号："))
        self.label_3.setText(_translate("Form_add", "姓名："))
        self.label_4.setText(_translate("Form_add", "成绩："))
        self.pushButton.setText(_translate("Form_add", "返回首页"))
        self.pushButton_2.setText(_translate("Form_add", "确认保存"))
