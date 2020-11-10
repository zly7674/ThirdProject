# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sort_student.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
class student:
    def __init__(self):
        self.num=''
        self.id=''
        self.score=0
stulist=[]
class Ui_Form_sort(object):
    def setupUi(self, Form_sort):
        Form_sort.setObjectName("Form_sort")
        Form_sort.resize(623, 506)
        self.lineEdit = QtWidgets.QLineEdit(Form_sort)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 281, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Form_sort)
        self.textEdit.setGeometry(QtCore.QRect(150, 80, 291, 331))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form_sort)
        self.pushButton.setGeometry(QtCore.QRect(230, 440, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sort)
        self.retranslateUi(Form_sort)
        QtCore.QMetaObject.connectSlotsByName(Form_sort)
        #self.read()
    def sort(self):
        db = pymysql.connect('localhost', 'root', '285300', 'student')
        cur = db.cursor()
        sql = "select * from info"
        cur.execute(sql)
        first = cur.fetchall()
        for i in first:
            stu = student()
            stu.num = i[0]
            stu.id = i[1]
            stu.score = i[2]
            print(i[0], i[1], i[2])
            stulist.append(stu)
        for i in range(len(stulist) - 1):
            flag = 0
            for j in range(len(stulist) - 1 - i):
                if int(stulist[j].score) < int(stulist[j + 1].score):
                    temp = stulist[j]
                    stulist[j] = stulist[j + 1]
                    stulist[j + 1] = temp
                    flag = 1
                if flag == 0:
                    break
        for i in stulist:
            self.textEdit.append(str(i.num)+'\t'+str(i.id)+'\t'+str(i.score))

    def read(self):
        self.aaa = '请先更新学生数据'
        self.textEdit.setText(self.aaa)
    def retranslateUi(self, Form_sort):
        _translate = QtCore.QCoreApplication.translate
        Form_sort.setWindowTitle(_translate("Form_sort", "学生信息管理系统"))
        self.lineEdit.setText(_translate("Form_sort", "学号      姓名     成绩"))
        self.pushButton.setText(_translate("Form_sort", "更新数据"))
