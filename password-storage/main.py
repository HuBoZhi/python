#<--*-- coding:utf-8 --*-->

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QFileDialog

from login import Ui_form_in
from logon import Ui_form_on
from Main_Form import Ui_form_Main_Form
from DataDeal import *
import sys

class Login(QMainWindow,Ui_form_in):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.LOGIN.clicked.connect(self.LongIn)

    def Open(self):
        self.show()
    def Get(self,user):
        self.username.setText(user["username"])
        self.password.setText(user["password"])

    def LongIn(self):
        username = self.username.text()
        password = self.password.text()
        if username=="":
            QMessageBox.warning(self,"警告","用户名不能为空！")
        else :
            if password=="":
                QMessageBox.warning(self,"警告","密码不能为空！")
            else:
                user = {
                    "username":username,
                    "password":password
                }
                f = CheckLoginData(user)
                if f==1:
                    self.OpenMain.emit(1)
                else:
                    if f==0:
                        QMessageBox.warning(self, "警告", "密码错误！")
                    else:
                        if f==-1:
                            QMessageBox.warning(self,"警告","用户不存在")

class Logon(QMainWindow,Ui_form_on):
    def __init__(self):
        super(Logon, self).__init__()
        self.setupUi(self)
        self.OK.clicked.connect(self.GetData)

    def GetData(self):
        #数据获取
        username =  self.username.text()
        password = self.password.text()
        repassword = self.repassword.text()
        f = CheckLogonData(self,username,password,repassword)
        if f == -1:
            self.username.setText('')
        else:
            if f==1:
                user = {
                    "username": username,
                    "password": password
                }
                writeData(user)#数据存入文件
                self.username.setText('')
                self.password.setText('')
                self.repassword.setText('')
                self.close()
                self.user.emit(user)

    def Open(self):
        print("LogonOpen")
        self.show()

class Main_Form(QMainWindow,Ui_form_Main_Form):
    def __init__(self):
        super(Main_Form, self).__init__()
        self.setupUi(self)
        self.fileOpen.triggered.connect(self.openMsg)  # 菜单的点击事件是triggered
        self.Save_as.triggered.connect(self.openMsgAndSave_as)
        self.fileSave.triggered.connect(self.openMsgAndSave)
        self.About.triggered.connect(self.AboutInformation)
        self.New.triggered.connect(self.NewCode)
        self.new_2.triggered.connect(self.NewGroup)
    def NewCode(self):
        print("NewCode")
    def NewGroup(self):
        print("NewGroup")
    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "E:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)  # 在状态栏显示文件地址
    def openMsgAndSave(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "E:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)  # 在状态栏显示文件地址
    def openMsgAndSave_as(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "E:/", "All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)  # 在状态栏显示文件地址


    def AboutInformation(self):
        QMessageBox.information(self,"About","本项目由胡博智个人于2018年二月份开始设计并完成。")
    def Open(self,f):
        #print("MainOpen")
        if f==1:
            self.show()
    def Close(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Show_login = Login()
    Show_logon = Logon()
    Show_Main_Form = Main_Form()
    #Show_login.show()
    Show_Main_Form.show()
    Line(Show_login,Show_logon,Show_Main_Form)
    sys.exit(app.exec_())
