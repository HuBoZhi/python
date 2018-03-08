#<--*-- coding:utf-8 --*-->

from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QFileDialog, QTableWidgetItem
from ADD import Ui_Add
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
        if f ==1:
            user = {
                "username": username,
                "password": password
            }
            self.close()
            self.user.emit(user)

    def Open(self):
        #print("LogonOpen")
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
        self.add = Add()
        self.table = Table()
        self.TABLE()
    def TABLE(self):
        self.Table.addWidget(self.table)
        self.table.show()
    def NewCode(self):
        self.Newcode.addWidget(self.add)
        self.table.close()
        self.add.show()
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
        if f==1: self.show()
    def Close(self):
        self.close()
class Add(QMainWindow,Ui_Add):
    def __init__(self):
        super(Add,self).__init__()
        self.setupUi(self)
        self.add.clicked.connect(self.ADD)
    def ADD(self):
        net = self.net.text()
        name = self.username.text()
        password = self.password.text()
        fname = "E:\Python学习\小程序\密码存储\Code"
        f = open(fname,"a")
        user = net+"\t"+name+"\t"+password+'\n'
        f.write(user)
        f.close()
        self.close()
from Table import Ui_Table
class Table(QMainWindow,Ui_Table):
    def __init__(self):
        super(Table,self).__init__()
        self.setupUi(self)
        self.table()
    def Close(self):
        self.close()
    def table(self):
        fname = "E:\Python学习\小程序\密码存储\Code"
        f = open(fname, "r")
        Lines = f.readlines()
        RowCount = len(Lines) + 1
        self.tableWidget.setRowCount(RowCount)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0, 199)
        self.tableWidget.setColumnWidth(1, 170)
        self.tableWidget.setColumnWidth(2, 199)
        self.tableWidget.setRowHeight(0, 30)
        for i in range(1, 3):
            self.tableWidget.setRowHeight(i, 40)
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.tableWidget.horizontalHeader().setVisible(False)
        Blank = "                ";L = ["网址", "账户", "密码"];count = 0
        for Value in L:
            self.tableWidget.setItem(0, count, QTableWidgetItem(Blank + Value))
            count += 1
        j = 1
        for data in Lines:
            i = 0
            data = data.strip('\n').split('\t')
            #net = data[0];username = data[1];password =data[2]
            for v in data:
                self.tableWidget.setItem(j, i, QTableWidgetItem(data[i]))
                i+=1
            j+=1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Show_login = Login()
    Show_logon = Logon()
    Show_Main_Form = Main_Form()
    Add = Add()
    Table = Table()
    #Show_login.show()
    Show_Main_Form.show()
    Line(Show_login,Show_logon,Show_Main_Form,Add,Table)
    sys.exit(app.exec_())