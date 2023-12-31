# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
    def initUi(self):
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        self.setStyleSheet("background-color:rgb(255,255,255);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.listView = QtWidgets.QListView(self.widget_2)
        self.listView.setObjectName("listView")
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        self.verticalLayout_2.addWidget(self.listView)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(200, 120))
        self.widget_5.setStyleSheet("border:1px solid;")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.widget_5)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_11.setStyleSheet("border:none;")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.widget_4 = QtWidgets.QWidget(self.widget_5)
        self.widget_4.setStyleSheet("border:none;")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.EditSend = QtWidgets.QLineEdit(self.widget_4)
        self.EditSend.setMinimumSize(QtCore.QSize(0, 30))
        self.EditSend.setMaximumSize(QtCore.QSize(16777215, 30))
        self.EditSend.setStyleSheet("border:1px solid;")
        self.EditSend.setObjectName("EditSend")
        self.horizontalLayout_3.addWidget(self.EditSend)
        self.SendButton = QtWidgets.QPushButton(self.widget_4)
        self.SendButton.setMinimumSize(QtCore.QSize(100, 30))
        self.SendButton.setMaximumSize(QtCore.QSize(100, 30))
        self.SendButton.setStyleSheet("border: 1px solid;\n"
"background-color: rgb(255, 255, 255);")
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout_3.addWidget(self.SendButton)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget_3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Node1ID = QtWidgets.QLineEdit(self.widget_3)
        self.Node1ID.setObjectName("Node1ID")
        self.verticalLayout.addWidget(self.Node1ID)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.Node2ID = QtWidgets.QLineEdit(self.widget_3)
        self.Node2ID.setObjectName("Node2ID")
        self.verticalLayout.addWidget(self.Node2ID)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.CANgatewayIP = QtWidgets.QLineEdit(self.widget_3)
        self.CANgatewayIP.setObjectName("CANgatewayIP")
        self.verticalLayout.addWidget(self.CANgatewayIP)
        self.SaveAndConnectButton = QtWidgets.QPushButton(self.widget_3)
        self.SaveAndConnectButton.setObjectName("SaveAndConnectButton")
        # self.SaveAndConnectButton.setStyleSheet("background-color: rgba(241,241,241,1);border:none;")
        self.SaveAndConnectButton.setMinimumHeight(30)
        self.verticalLayout.addWidget(self.SaveAndConnectButton)
        self.DisConnectButton = QtWidgets.QPushButton(self.widget_3)
        self.DisConnectButton.setObjectName("SaveAndConnectButton")
        self.DisConnectButton.setText("Disconnect")
        self.DisConnectButton.setMinimumHeight(30)
        self.DisConnectButton.setStyleSheet("background-color: rgba(241,241,241,1);border:none;")
        self.verticalLayout.addWidget(self.DisConnectButton)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.PresetButton = QtWidgets.QPushButton(self.widget_3)
        self.PresetButton.setObjectName("PresetButton")
        self.verticalLayout.addWidget(self.PresetButton)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.Node1 = QtWidgets.QLineEdit(self.widget_3)
        self.Node1.setObjectName("Node1")
        self.verticalLayout.addWidget(self.Node1)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.Node2 = QtWidgets.QLineEdit(self.widget_3)
        self.Node2.setObjectName("Node2")
        self.verticalLayout.addWidget(self.Node2)
        self.RunButton = QtWidgets.QPushButton(self.widget_3)
        self.RunButton.setObjectName("RunButton")
        self.verticalLayout.addWidget(self.RunButton)
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_12.setText(_translate("Form", "Received/Sent data/Status"))
        self.label_11.setText(_translate("Form", "Manually send data"))
        self.SendButton.setText(_translate("Form", "Send"))
        self.label.setText(_translate("Form", "Setup"))
        self.label_2.setText(_translate("Form", "Can baud"))
        self.comboBox.setItemText(0, _translate("Form", "800000"))
        self.comboBox.setItemText(1, _translate("Form", "250000"))
        self.comboBox.setItemText(2, _translate("Form", "400000"))
        self.comboBox.setItemText(3, _translate("Form", "500000"))
        self.label_3.setText(_translate("Form", "Node 1 ID"))
        self.label_4.setText(_translate("Form", "Node 2 ID"))
        self.label_5.setText(_translate("Form", "CAN gateway IP"))
        self.SaveAndConnectButton.setText(_translate("Form", "Save and Connect"))
        self.label_6.setText(_translate("Form", "Pre-Opeation"))
        self.PresetButton.setText(_translate("Form", "Preset"))
        self.label_7.setText(_translate("Form", "Resolution"))
        self.label_8.setText(_translate("Form", "Node 1"))
        self.label_9.setText(_translate("Form", "Node 2"))
        self.RunButton.setText(_translate("Form", "Run"))
        self.label_10.setText(_translate("Form", "Operation"))
        self.pushButton_4.setText(_translate("Form", "Back to Pre-Opeation"))
