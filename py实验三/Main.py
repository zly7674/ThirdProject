from PyQt5 import QtWidgets,QtGui,QtCore
from main_student import Ui_Form_main
from add_student import Ui_Form_add
from del_student import Ui_Form_del
from chec_student import Ui_Form_check
from mod_student import Ui_Form_mod



import sys
class Main(QtWidgets.QMainWindow,Ui_Form_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_show)
        self.pushButton_1.clicked.connect(self.del_show)
        self.pushButton_2.clicked.connect(self.chec_show)
        self.pushButton_3.clicked.connect(self.mod_show)
        self.pushButton_4.clicked.connect(self.exit_main)
    def add_show(self):
        self.add=Main_add()
        self.add.show()
    def del_show(self):
        self.dele=Main_del()
        self.dele.show()
    def chec_show(self):
        self.chec=Main_chec()
        self.chec.show()
    def mod_show(self):
        self.mod=Main_mod()
        self.mod.show()
    def exit_main(self):
        exit()

class Main_add(QtWidgets.QMainWindow,Ui_Form_add):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Main_del(QtWidgets.QMainWindow,Ui_Form_del):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class Main_chec(QtWidgets.QMainWindow,Ui_Form_check):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
class Main_mod(QtWidgets.QMainWindow,Ui_Form_mod):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #使窗体按照Qt设计显示
app=QtWidgets.QApplication(sys.argv)
main=Main()
main.show()
sys.exit(app.exec_())