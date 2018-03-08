# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_in(object):
    OpenMain = QtCore.pyqtSignal(int)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.LOGON = QtWidgets.QPushButton(self.centralwidget)
        self.LOGON.setGeometry(QtCore.QRect(100, 190, 140, 40))
        self.LOGON.setObjectName("LOGON")
        self.LOGIN = QtWidgets.QPushButton(self.centralwidget)
        self.LOGIN.setGeometry(QtCore.QRect(260, 190, 140, 40))
        self.LOGIN.setObjectName("LOGIN")

        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(170, 60, 230, 30))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(170, 110, 230, 30))
        self.password.setObjectName("password")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 120, 45, 19))
        self.label.setMinimumSize(QtCore.QSize(45, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 61, 20))
        self.label_2.setMinimumSize(QtCore.QSize(45, 19))
        self.label_2.setObjectName("label_2")

        self.username.raise_()
        self.password.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.LOGON.raise_()
        self.LOGIN.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "密码存储"))
        self.LOGON.setText(_translate("MainWindow", "注   册"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">密码:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">用户名:</span></p></body></html>"))
        self.LOGIN.setText(_translate("MainWindow", "登   录"))
'''
def OpenLogin():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_form_in()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
OpenLogin()
'''