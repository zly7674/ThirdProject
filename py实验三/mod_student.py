# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mod_student.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from del_student import *
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form_mod(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 606)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 120, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 240, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(220, 230, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 320, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 320, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(111, 410, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 400, 221, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 500, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 500, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.mod)
        self.pushButton_2.clicked.connect(self.close)
    def mod(self):
        print('修改')
        s1=(self.lineEdit.text())
        s2=(self.lineEdit_2.text())
        s3=(self.lineEdit_3.text())
        # 连接数据库
        db = pymysql.connect('localhost', 'root', '285300', 'student')
        cur = db.cursor()
        sql = "update info set id = '%s',score=%d where num = '%s';"%(s2,int(s3),s1)
        t=cur.execute(sql)
        db.commit()
        if t==1:
            mbox = QtWidgets.QMessageBox
            mbox.question(self, "标题", "修改成功", mbox.Ok)
        else :
            mbox = QtWidgets.QMessageBox
            mbox.question(self, "标题", "修改失败", mbox.Ok)
        print(t)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学生信息管理系统"))
        self.label.setText(_translate("Form", "修改学生信息"))
        self.label_2.setText(_translate("Form", "待修改学号："))
        self.label_3.setText(_translate("Form", "新姓名："))
        self.label_4.setText(_translate("Form", "新成绩："))
        self.pushButton.setText(_translate("Form", "确认修改"))
        self.pushButton_2.setText(_translate("Form", "返回首页"))
