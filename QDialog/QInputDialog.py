from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

class Window(QtWidgets.QInputDialog):
    def __init__(self):
        super().__init__()

    def msg(self):
        intnum,ok=QInputDialog.getInt(self,'标题','计数：',30,-10000,10000,2)
        print(intnum,ok)

    def msg1(self):
        text,ok1=QInputDialog.getText(self,'输入文本框','请输入文本内容',QLineEdit.Normal,'默认文字')
        print(text,ok1)
    def msg2(self):
        items=['B18511','B18512']
        item,ok2=QInputDialog.getItem(self,'标题','班级',items,0,False)
        print(item,ok2)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.msg()
    #window.msg1()
    # window.msg2()
    #sys.exit(app.exec_())
