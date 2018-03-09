#< -*- coding:utf-8 -*->

# 数据检测
from PyQt5.QtWidgets import QMessageBox

def CheckLoginData(user):
    fname = "E:\Python 学习\小程序\密码存储\init"
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
    fname = "E:\Python 学习\小程序\密码存储\init"
    f = open(fname, 'r')
    sourceInLines = f.readlines()  # 按行读出文件内容
    f.close()

    if username == "":
        QMessageBox.warning(self, "警告", "用户不能为空！")
    else:
        for line in sourceInLines:
            temp = line.strip('\n')  # 去掉每行最后的换行符'\n'
            temp_name = temp.split(':')[0]  # 以'  '为标志，将每行分割成列表
            if temp_name==username:
                QMessageBox.warning(self,"警告","用户已存在！")
                return -1
        else:
            if password == "":
                QMessageBox.warning(self, "警告", "密码不能为空！")
            else:
                if repassword == "":
                    QMessageBox.warning(self, "警告", "请重新输入密码！")
                else:
                    if repassword == password:
                        return 1
                    else:
                        QMessageBox.warning(self, "警告", "密码不一致！")
# 数据传到登录界面
def Line(Myshow1,Myshow2,Myshow3):
    Myshow1.LOGON.clicked.connect(Myshow2.Open)
    Myshow2.user.connect(Myshow1.Get)
    Myshow1.OpenMain.connect(Myshow3.Open)
    Myshow3.new_user.triggered.connect(Myshow1.Open)
# 数据写入到文件
def writeData(User):
    line = User['username']+":"+User['password']
    fname = "E:\Python 学习\小程序\密码存储\init"
    try:
        fobj = open(fname,'a')                 # 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
    except IOError:
        print (fname+'open error!')
    else:
        fobj.write(line+'\n')               #这里的\n的意思是在源文件末尾换行。
        fobj.close()                        #特别注意文件操作完毕后要close