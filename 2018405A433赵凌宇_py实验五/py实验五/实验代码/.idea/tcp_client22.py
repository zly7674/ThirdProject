from PyQt5 import QtWidgets,QtGui,QtCore
import sys
from socket import *
from client_interface import Ui_Form

from bll import *
# import json

# 创建套接字
sockfd = socket()
class Main(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.record = Records()
        self.pushButton.clicked.connect(self.lianjie)
        self.pushButton_2.clicked.connect(self.fasong)
        self.pushButton_3.clicked.connect(self.jieshou)
        self.pushButton_4.clicked.connect(self.qingping)
    def lianjie(self):
        # 发起连接
        server_addr = ('192.168.1.3',a)
        sockfd.connect(server_addr)
        self.textEdit.append('连接成功！！')
    def fasong(self):
        self.num1 = self.lineEdit.text()
        self.num2 = self.lineEdit_2.text()
        print(self.num2+':'+self.num1)
        self.record.id = self.num2
        self.record.send = self.num1
        sockfd.send((self.num2+':'+self.num1).encode())
        self.textEdit.append(self.num2+':'+self.num1)
    def jieshou(self):
        data = sockfd.recv(1024)
        self.textEdit.append('服务器:'+data.decode())
        self.record.answer = data.decode()
        save(self.record)
    def qingping(self):
        self.textEdit.clear()




QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #使窗体按照Qt设计显示
app=QtWidgets.QApplication(sys.argv)
main=Main()
main.show()
sys.exit(app.exec_())
#关闭套接字
sockfd.close()
