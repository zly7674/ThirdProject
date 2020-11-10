from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from QDialog.QLineEdit_QTextEdit import Ui_Form
import sys
class Main_QLineEdit_QTextEdit(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.prn)
        self.pushButton_2.clicked.connect(self.clear)
    def settext(self):
        self.lineEdit.setText('单行文本框')
        self.textEdit.setPlainText(a)
    def prn(self):
        line = self.lineEdit.text()
        print(line)
        text = self.textEdit.toPlainText()
        print(text)
    def clear(self):
        self.lineEdit.clear()
        self.textEdit.clear()
if __name__=='__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    main=Main_QLineEdit_QTextEdit()
    main.settext()
    main.show()
    sys.exit(app.exec_())