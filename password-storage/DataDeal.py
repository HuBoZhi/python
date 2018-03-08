#< -*- coding:utf-8 -*->

# 数据检测
from PyQt5.QtWidgets import QMessageBox

def CheckLoginData(user):
    fname = "E:\Python学习\小程序\密码存储\init"
    f = open(fname,'r')
    sourceInLines = f.readlines()  # 按行读出文件内容
    f.close()
    for line in sourceInLines:
        temp = line.strip('\n')  # 去掉每行最后的换行符'\n'
        temp_name = temp.split(':')[0]  # 以'  '为标志，将每行分割成列表
        #print(temp_name)
        temp_pass = temp.split(':')[1]
        #print(temp_pass)
        if temp_name==user['username']:
            if temp_pass!=user['password']:
                return 0
            else:
                return 1
    return -1
def CheckLogonData(self,username,password,repassword):
    fname = "E:\Python学习\小程序\密码存储\init"
    f = open(fname,"a+")
    sourceInLines = f.readlines()  # 按行读出文件内容

    if username == "":
        QMessageBox.warning(self, "警告", "用户不能为空！")
    else:
        for line in sourceInLines:
            temp = line.strip('\n')  # 去掉每行最后的换行符'\n'
            temp_name = temp.split(':')[0]# 以'  '为标志，将每行分割成列表
            if temp_name==username:
                QMessageBox.warning(self,"警告","用户已存在！")
                self.username.setText('')
                # return -1
        if password == "":
            QMessageBox.warning(self, "警告", "密码不能为空！")
        if repassword == "":
            QMessageBox.warning(self, "警告", "请重新输入密码！")
        if repassword == password:
            user = username + ":" + password
            f.write(user + '\n')
            f.close()
            return 1
        else:
            QMessageBox.warning(self, "警告", "密码不一致！")
# 数据传到登录界面
def Line(Myshow1,Myshow2,Myshow3,Myshow4,Myshow5):
    Myshow1.LOGON.clicked.connect(Myshow2.Open)
    Myshow2.user.connect(Myshow1.Get)
    Myshow1.OpenMain.connect(Myshow3.Open)
    Myshow3.new_user.triggered.connect(Myshow1.Open)
