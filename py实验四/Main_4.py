from PyQt5 import QtWidgets,QtCore,QtGui
from main import Ui_Form_main
from load_user import Ui_Form_load
from register_user import Ui_Form_reg

import sys

class Main(QtWidgets.QMainWindow,Ui_Form_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load_show)
        self.pushButton_2.clicked.connect(self.reg_show)
    def load_show(self):
        self.load=Main_load()
        self.load.show()
    def reg_show(self):
        self.reg=Main_reg()
        self.reg.show()
class Main_load(QtWidgets.QMainWindow, Ui_Form_load):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
class Main_reg(QtWidgets.QMainWindow,Ui_Form_reg):
     def __init__(self):
        super().__init__()
        self.setupUi(self)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #使窗体按照Qt设计显示
app=QtWidgets.QApplication(sys.argv)
main=Main()
main.show()
sys.exit(app.exec_())