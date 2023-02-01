# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(201, 284)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/clipart2261836.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.name_text = QtWidgets.QTextEdit(self.centralwidget)
        self.name_text.setMaximumSize(QtCore.QSize(189, 200))
        self.name_text.setObjectName("name_text")
        self.verticalLayout.addWidget(self.name_text)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.combo_role = QtWidgets.QComboBox(self.centralwidget)
        self.combo_role.addItems(['Танк', 'Хил', 'ДД'])
        font = QtGui.QFont()
        font.setPointSize(14)
        self.combo_role.setFont(font)
        self.combo_role.setObjectName("combo_role")
        self.verticalLayout.addWidget(self.combo_role)
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_add.setFont(font)
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление персонажа"))
        self.label.setText(_translate("MainWindow", "Ник"))
        self.label_2.setText(_translate("MainWindow", "Роль"))
        self.button_add.setText(_translate("MainWindow", "Добавить"))
