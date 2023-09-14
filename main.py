from ui.ui import Ui_App
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import QColor,QPixmap,QImage
from PyQt5.QtCore import QPoint,QRect,QSize
import sys,os,cv2


class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_App()
        self.ui.setupUi(self)
        self.show()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainApplication()
    sys.exit(app.exec_())