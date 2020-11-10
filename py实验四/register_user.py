# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_user.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import user
import pymysql

class Ui_Form_reg(object):
    def setupUi(self, Form_reg):
        Form_reg.setObjectName("Form_reg")
        Form_reg.resize(620, 525)
        self.label = QtWidgets.QLabel(Form_reg)
        self.label.setGeometry(QtCore.QRect(230, 80, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_reg)
        self.label_2.setGeometry(QtCore.QRect(90, 155, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form_reg)
        self.label_3.setGeometry(QtCore.QRect(90, 250, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form_reg)
        self.lineEdit.setGeometry(QtCore.QRect(210, 160, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form_reg)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 250, 241, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form_reg)
        self.pushButton.setGeometry(QtCore.QRect(180, 360, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form_reg)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 360, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form_reg)
        QtCore.QMetaObject.connectSlotsByName(Form_reg)

        self.pushButton.clicked.connect(self.reg_user)
        self.pushButton_2.clicked.connect(self.close)
    def reg_user(self):
        flag = 0
        id=self.lineEdit.text()
        pwd=self.lineEdit_2.text()
        ulist=list(user.first)
        for i in ulist:
            if id==i[0]:
                mbox = QtWidgets.QMessageBox
                mbox.question(self, "标题", "用户名重复", mbox.Ok)
                print("用户名重复")
                flag = 1
        if flag==0:
            print("插入到user数据表中")
            db=pymysql.connect('localhost','root','285300','user')
            cur=db.cursor()
            sql="insert into info(id,pwd) values('%s', '%s');"%(id,pwd)
            print(sql)
            try :
                cur.execute(sql)
                db.commit()
                mbox = QtWidgets.QMessageBox
                mbox.question(self, "标题", "添加成功", mbox.Ok)
            except Exception as e:
                db.rollback()  # 失败回滚到操作之前的状态
                print("Faild:",e)
                mbox = QtWidgets.QMessageBox
                mbox.question(self, "标题", "用户名重复", mbox.Ok)
                cur.close()
                db.close()


    def retranslateUi(self, Form_reg):
        _translate = QtCore.QCoreApplication.translate
        Form_reg.setWindowTitle(_translate("Form_reg", "注册界面"))
        self.label.setText(_translate("Form_reg", "     用户注册"))
        self.label_2.setText(_translate("Form_reg", "用户名："))
        self.label_3.setText(_translate("Form_reg", "密码："))
        self.pushButton.setText(_translate("Form_reg", "确认注册"))
        self.pushButton_2.setText(_translate("Form_reg", "退出"))
