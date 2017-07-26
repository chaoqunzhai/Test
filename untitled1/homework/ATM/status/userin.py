#!_*_coding:utf-8_*_
import json
import os
user_status = False

def login(func):
    def usersing():
        while True:
            global user_status
            path1 = os.path.abspath('..')
            file_path = os.path.join(path1, 'db', 'userup_db')
            write_path = os.path.join(path1,'status','typle')
            if os.path.exists(file_path):
                f = open(file_path, 'r', encoding='utf-8')
                data = json.load(f)
                print('\033[33m--登录栏目(q为退出)--\033[0m')
                _username = input('username>>').strip()
                if _username == 'q':
                    print('\033[33m--成功退出--\033[0m')
                    break
                _password = input('password>>').strip()
                if _password == 'q':
                    print('\033[33m--成功退出--\033[0m')
                    break
                if _username == data['name'] and _password == data['password']:
                    print('\033[34m欢迎您登陆成功\033[0m')
                    user_status = True
                    f1 = open(write_path,'w',encoding='utf-8')
                    data2= 'True'
                    f1.write(json.dumps(data2))
                    f1.close()
                    break
                else:
                    print('\033[34m登陆失败\033[0m')
                if user_status == True:
                    func()
            else:
                print('\033[31m，现阶段处于未注册，请先注册！\033[0m')
                break
    return usersing

