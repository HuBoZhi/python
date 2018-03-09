# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ADD.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 470)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.add = QtWidgets.QPushButton(self.centralwidget)

        self.add.setGeometry(QtCore.QRect(430, 380, 100, 40))
        self.add.setObjectName("add")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 80, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 80, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 250, 80, 30))
        self.label_3.setObjectName("label_3")

        self.net = QtWidgets.QLineEdit(self.centralwidget)
        self.net.setGeometry(QtCore.QRect(160, 60, 250, 30))
        self.net.setObjectName("net")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(160, 160, 250, 30))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(160, 250, 250, 30))
        self.password.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add.setText(_translate("MainWindow", "添  加"))
        self.add.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.label.setText(_translate("MainWindow", "网  址："))
        self.label_2.setText(_translate("MainWindow", "账  户："))
        self.label_3.setText(_translate("MainWindow", "密  码："))

