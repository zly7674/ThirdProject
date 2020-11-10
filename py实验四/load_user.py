# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load_user.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
class Ui_Form_load(object):
    def setupUi(self, Form_load):
        Form_load.setObjectName("Form_load")
        Form_load.resize(594, 524)
        self.label = QtWidgets.QLabel(Form_load)
        self.label.setGeometry(QtCore.QRect(230, 80, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_load)
        self.label_2.setGeometry(QtCore.QRect(80, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_load)
        self.label_3.setGeometry(QtCore.QRect(80, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form_load)
        self.lineEdit.setGeometry(QtCore.QRect(202, 180, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form_load)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 270, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form_load)
        self.pushButton.setGeometry(QtCore.QRect(160, 360, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form_load)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 360, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form_load)
        QtCore.QMetaObject.connectSlotsByName(Form_load)

        self.pushButton.clicked.connect(self.load_u)
        self.pushButton_2.clicked.connect(self.close)

    def load_u(self):
        name=self.lineEdit.text()
        num=self.lineEdit_2.text()
        flag=1
        db = pymysql.connect('localhost', 'root', '285300', 'user')
        cur = db.cursor()
        sql = "select * from info;"
        cur.execute(sql)
        ulist = cur.fetchall()
        db.commit()
        cur.close()
        db.close()
        ulist=list(ulist)
        for i in ulist:
            if i[0]==name and i[1]==num:
                print("登录成功")
                mbox = QtWidgets.QMessageBox
                mbox.question(self, "标题", "登录成功", mbox.Ok)
                flag = 0

        if flag == 1:
            mbox = QtWidgets.QMessageBox
            mbox.question(self, "标题", "输入信息有误", mbox.Ok)
    def retranslateUi(self, Form_load):
        _translate = QtCore.QCoreApplication.translate
        Form_load.setWindowTitle(_translate("Form_load", "登录界面"))
        self.label.setText(_translate("Form_load", "  用户登录"))
        self.label_2.setText(_translate("Form_load", "用户名："))
        self.label_3.setText(_translate("Form_load", " 密码："))
        self.pushButton.setText(_translate("Form_load", "确认登录"))
        self.pushButton_2.setText(_translate("Form_load", "退出"))
