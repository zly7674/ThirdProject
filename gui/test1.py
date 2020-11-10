'''
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
first_window = QtWidgets.QWidget()
first_window.resize(800,600)
first_window.setWindowTitle("我的第一个程序")
first_window.show()
sys.exit(app.exec_())
'''

from PyQt5 import QtWidgets
class FirstWindow(QtWidgets.QWidget):
    def __init__(self):
       super(FirstWindow,self).__init__()
       #super().__init__()

def mainwindow():
      import sys
      app = QtWidgets.QApplication(sys.argv)
      window = FirstWindow()
      window.show()
      sys.exit(app.exec_())

if __name__=="__main__":
    mainwindow()