from PyQt5 import QtWidgets,QtGui,QtCore
from interfance import Ui_Form_interfance
from add import Ui_Form_add
import sys
class Main(QtWidgets.QMainWindow,Ui_Form_interfance):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_show)
    def add_show(self):
        self.add=Main_add()
        self.add.show()

class Main_add(QtWidgets.QMainWindow,Ui_Form_add):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling) #使窗体按照Qt设计显示
app=QtWidgets.QApplication(sys.argv)
main=Main()
main.show()
sys.exit(app.exec_())
