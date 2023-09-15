from ui.ui import Ui_App
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtGui import QColor,QPixmap,QImage
from PyQt5.QtCore import QPoint,QRect,QSize
import sys,os,cv2

from datetime import datetime
from process import *
class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.isSucces = False
        self.client_socket = None
        self.setWindowTitle("CANOpem Gateway")  
        self.ui = Ui_App()
        self.ui.setupUi(self)
        self.show()
        self.ui.send.SaveAndConnectButton.clicked.connect(self.connectIP)
        self.ui.send.SendButton.clicked.connect(self.sendData)
    def sendData(self):
        if(self.isSucces):
            if(len(self.ui.send.EditSend.text()) > 0):
                message = send_data(self.client_socket,self.ui.send.EditSend.text())
                self.addToList("["+timeNow+"]:"+message)
            else:
                timeNow = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                self.addToList("["+timeNow+"]:Không có dữ liệu gửi đi !")
        else:
            timeNow = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            self.addToList("["+timeNow+"]:Gửi dữ liệu thất bại !")
        
            
        
    def addToList(self,str):
        new_item = QtGui.QStandardItem(str)
        self.ui.send.model.appendRow(new_item)
        self.ui.send.listView.setCurrentIndex(self.ui.send.model.indexFromItem(new_item))
    def closeEvent(self,event):
        disconnect_device(self.isSucces,self.client_socket)
        self.close()

    def connectIP(self):
        if(len(self.ui.send.CANgatewayIP.text()) > 0):
            self.isSucces,self.client_socket = connect_device(self.ui.send.CANgatewayIP.text())
            if(self.isSucces):
                timeNow = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                self.ui.send.label_12.setText("["+timeNow+"]:Kết nối thành công !")
            else:
                self.ui.send.label_12.setText("Kết nối thành công !")
        else:
            timeNow = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            self.ui.send.label_12.setText("["+timeNow+"]:CAN getway IP trống. Vui lòng nhập!")
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainApplication()
    sys.exit(app.exec_())