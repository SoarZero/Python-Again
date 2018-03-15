#！/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
import getpass


#作业要求编写登陆窗口
#输入用户名密码
#认证成功显示欢迎信息
#输错三次锁定

#登陆 注册
#user_name = open("User_Name.log","w")     #创建一个用户名文件 只能用一种模式打开
#user_name.close()

#user_password = open("User_Password.log","w")   #创建一个用户密码文件
#user_password.close()

#lock_user = open("Lock_User.log","w")      #创建一个被锁定用户文件
#lock_user.close()

#用户注册
#print("请输入login？还是register？")
while True :
    chose = input("请输入l？还是r？")             #选择
    if chose == 'l' :
        print("登陆")
        Name = input("请输入用户名：")
        print(Name)
        user_name = open("User_Name.log", 'r')               #读文件
        user_password = open("User_Password.log", 'r')       #同上
        lock_user = open("Lock_User.log","r")                #同上
        user_name_list = user_name.readlines()                #将列表转换为列表格式
        user_password_list = user_password.readlines()        #同上
        lock_user_list = lock_user.readlines()                #同上
        #Append_format =
        #passwd = user_name_list.index(Name)     # 索引对应名字的序号
        #print("他的名字：", passwd)
        for Lock_List in lock_user_list :                    #循环读出每一个字符串
            lock_list = Lock_List.strip('\n')                #去除字符串中的（\n）
            if Name == lock_list :
                sys.exit("对不起，%s 已经被锁定，不能登陆"%(Name))
            else:
                print("user_name%s user_password%s Lock_user %s"%(user_name_list,user_password_list,lock_user_list))
                i = 0
                for Name_List in user_name_list:                     #读出每一个字符串，便于处理
                    name_list = Name_List.strip('\n')                #对每一个字符串去除{\n}
                    print("次数: %d 用户名：%s"%(i,name_list))
                    if Name == name_list :                           #判断是否存在
                        count = 0
                        while count < 3:                              #三次机会
                            password = input("请输入密码:")
                            for Password_List in  user_password_list :   #读出每一个字符串
                                password_list = Password_List.strip('\n') #去除\n
                                if password == password_list:
                                    print("恭喜你登陆成功。")
                                    sys.exit(0)
                                else:
                                    continue                      #没有即结束这次循环
                            print("您输入的密码错误%s，还有%d次机会"%(Name,2-count))
                            count +=1
                        else:
                            lock_name = open("Lock_User.log","a")               #添加锁定账户
                            lock_name.write(Name + '\n')
                            lock_name.close()
                            sys.exit("您已经三次输入错误，您的帐号将被锁定。")
                    else:
                        pass
                    i +=1
                else:
                    pass
            print("--->",name_list)
        else:
            pass

    else:
        print("注册")
        user_name = open("User_Name.log",'a')
        name = input("请输入用户名：")
        user_name.write(name + '\n' )
        #print(user_name.readlines())
        #user_name.close()
        #user_name = open("User_Name.log", 'r')
        print("请确认用户名 %s"%(name))
        user_password = open("User_Password.log","a")
        password = input("请输入密码：")
        user_password.write(password + '\n')


    user_name.close()
    user_password.close()





'''
lock_file = open("account_lock","w")
lock_file.write("ZhangSan\n")
lock_file.write("ZhangSan1\n")
lock_file.write("ZhangSan2\n")
lock_file.close()

user_file = open("account","w")
user_file.write("wxl\n")
user_file.write("123456\n")
user_file.close()


i = 0
while i<3:
    name = input("请输入用户名：")

    lock_file = open("account_lock","r")
    lock_list = lock_file.readlines()

    for lock_line in lock_list:
        lock_line = lock_line.strip('\n')
        if name == lock_line:
            sys.exit("用户 %s 已经被锁定，退出"%(name))

    user_file = open("account","r")
    user_list = user_file.readlines()
    print(user_list)
    user = user_list[0].strip('\n')
    password = user_list[1].strip('\n')
    print("user:%s password%s"%(user,password))

    for user_line in user_list:
        #user = user_line.strip("\n").split()
        #password = user_line.strip("\n").split()
        #print("user %s password %s"%(user,password))

        if name == user :
            j = 0
            while j<3:
                passwd = input("请输入密码：")
                if passwd == password:
                    print("用户 %s 登陆成功"%(name))
                    sys.exit(0)
                else:
                    if j!=2 :
                        print("用户 %s 密码错误，请重新输入，还有%d 次机会"%(name,2-j))
                j +=1
            else:
                lock_file.write(name + "\n")
                sys.exit("用户 %s 达到最大登陆次数，将被锁定并退出"%(name))
        else:
            pass
    else:
        if i != 2:
            print("用户名 %s 不存在，请重新输入，还有%d次机会"%(name,2-i))
    i += 1
else:
    sys.exit("用户 %s 不存在，退出"%name)

lock_file.close()
user_file.close()
'''
