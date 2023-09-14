from PyQt5 import QtCore,QtWidgets,QtGui
from ui.send import Ui_Form

class Ui_App(object):
    def setupUi(self,App):
        App.setObjectName("Home")
        # App.resize(1104, 749)
        App.setStyleSheet("background-color: rgb(255, 255, 255);\n"
# "border:2px solid;\n"
"")             
        self.centralWidget = QtWidgets.QWidget(App)
        self.centralWidget.setGeometry(0,0,800,800)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
       
        self.tabWidget = QtWidgets.QTabWidget(App)
        self.send = Ui_Form()
        self.tabWidget.addTab(self.send,"")
        # self.tabWidget.setMinimumSize(QtCore.QSize(800,480))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setCurrentIndex(0)
        self.tabbar = self.tabWidget.findChild(QtWidgets.QTabBar)
        self.tabbar.hide()
        self.tabWidget.setMinimumSize(1104, 749)
        self.verticalLayout.addWidget(self.tabWidget)
        App.setCentralWidget(self.centralWidget)  