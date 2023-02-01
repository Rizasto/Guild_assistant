# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(268, 443)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/clipart2261836.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.list_chars = QtWidgets.QListView(self.centralwidget)
        self.list_chars.setObjectName("list_chars")
        self.gridLayout.addWidget(self.list_chars, 0, 0, 1, 2)
        self.button_delete = QtWidgets.QPushButton(self.centralwidget)
        self.button_delete.setObjectName("button_delete")
        self.gridLayout.addWidget(self.button_delete, 1, 1, 1, 1)
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setObjectName("button_add")
        self.gridLayout.addWidget(self.button_add, 1, 0, 1, 1)
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setObjectName("button_exit")
        self.gridLayout.addWidget(self.button_exit, 3, 1, 1, 1)
        self.button_update = QtWidgets.QPushButton(self.centralwidget)
        self.button_update.setObjectName("button_update")
        self.gridLayout.addWidget(self.button_update, 2, 0, 1, 1)
        self.button_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.button_refresh.setObjectName("button_refresh")
        self.gridLayout.addWidget(self.button_refresh, 2, 1, 1, 1)
        self.button_table = QtWidgets.QPushButton(self.centralwidget)
        self.button_table.setObjectName("button_table")
        self.gridLayout.addWidget(self.button_table, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RL Helper"))
        self.button_delete.setText(_translate("MainWindow", "Удалить"))
        self.button_add.setText(_translate("MainWindow", "Добавить"))
        self.button_exit.setText(_translate("MainWindow", "Выход"))
        self.button_update.setText(_translate("MainWindow", "Обновить БД"))
        self.button_refresh.setText(_translate("MainWindow", "Обновить список"))
        self.button_table.setText(_translate("MainWindow", "Создать таблицу"))
