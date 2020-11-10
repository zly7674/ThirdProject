# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chec_student.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from sort_student import Ui_Form_sort # 引用排序模块
import pymysql
class student:
    def __init__(self):
        self.num=''
        self.name=''
        self.score=0
class Ui_Form_check(object):
    def setupUi(self, Form_check):
        Form_check.setObjectName("Form_check")
        Form_check.resize(595, 581)
        self.label = QtWidgets.QLabel(Form_check)
        self.label.setGeometry(QtCore.QRect(190, 70, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form_check)
        self.textEdit.setGeometry(QtCore.QRect(140, 180, 281, 291))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form_check)
        self.pushButton.setGeometry(QtCore.QRect(142, 490, 151, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form_check)
        self.lineEdit.setGeometry(QtCore.QRect(142, 140, 281, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form_check)
        QtCore.QMetaObject.connectSlotsByName(Form_check)
        self.read()
        self.pushButton.clicked.connect(self.sort) #排序模块
    def sort(self):
        self.sort = chec_sort() #实例化
        self.sort.show()

    def read(self): #读文件，查询功能的实现
        list_s = []
        db = pymysql.connect('localhost', 'root', '285300', 'student')
        cur = db.cursor()
        sql = "select * from info"
        cur.execute(sql)
        first =cur.fetchall()
        for i in first:
            print(i[2])
            self.textEdit.append(str(i[0])+'\t'+str(i[1])+'\t'+str(i[2]))
        db.commit()
        cur.close()
        db.close()

    def retranslateUi(self, Form_check):
        _translate = QtCore.QCoreApplication.translate
        Form_check.setWindowTitle(_translate("Form_check", "学生成绩管理系统"))
        self.label.setText(_translate("Form_check", "查询学生成绩"))
        self.pushButton.setText(_translate("Form_check", "按成绩降序排列"))
        self.lineEdit.setText(_translate("Form_check", "学号     姓名       成绩"))

class chec_sort(QtWidgets.QMainWindow,Ui_Form_sort):
    def __init__(self):
        super().__init__()
        self.setupUi(self)