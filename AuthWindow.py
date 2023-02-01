# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Authorize.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.resize(325, 321)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/clipart2261836.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AuthWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AuthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.clientId = QtWidgets.QTextEdit(self.centralwidget)
        self.clientId.setObjectName("clientId")
        self.gridLayout.addWidget(self.clientId, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.clientSecret = QtWidgets.QTextEdit(self.centralwidget)
        self.clientSecret.setObjectName("clientSecret")
        self.gridLayout.addWidget(self.clientSecret, 3, 0, 1, 2)
        self.button_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_info.setObjectName("button_info")
        self.gridLayout.addWidget(self.button_info, 4, 0, 1, 1)
        self.button_auth = QtWidgets.QPushButton(self.centralwidget)
        self.button_auth.setObjectName("button_auth")
        self.gridLayout.addWidget(self.button_auth, 4, 1, 1, 1)
        AuthWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AuthWindow)
        self.statusbar.setObjectName("statusbar")
        AuthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Авторизация"))
        self.label.setText(_translate("AuthWindow", "Client ID"))
        self.label_2.setText(_translate("AuthWindow", "Client Secret"))
        self.button_info.setText(_translate("AuthWindow", "Инфо"))
        self.button_auth.setText(_translate("AuthWindow", "Авторизация"))
