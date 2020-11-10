from PyQt5 import QtWidgets
from layouts import Ui_Form
import sys
if __name__=="__main__":
  app=QtWidgets.QApplication(sys.argv)
  ui=Ui_Form()
  widget=QtWidgets.QWidget()
  ui.setupUi(widget)
  widget.show()
  sys.exit(app.exec_())