#_*_coding:utf-8_*_

import json
import os
import sys
UPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(UPDIR)

from conf import uuids

user_status = False
@uuids.uid
def userup():
    while True:
        print("\033[32m注册栏目(q为退出)\033[0m")
        path1 = os.path.abspath('..')
        username = input('username>>').strip()
        if username == 'q':
            print('\033[33m--成功退出--\033[0m')
            break
        password = input('password>>').strip()
        if password == 'q':
            print('\033[33m--成功退出--\033[0m')
            break
        logins = {'name': 'username', 'password': 'psword', 'credit': 'credit', 'balance': 'balance'}
        logins['name'] = username
        logins['password'] = password
        logins['credit'] = '15000'
        logins['balance'] = '15000'
        user_status =True
        print('\033[35m个人基本信息如下\033[0m')
        print(logins)
        print('\033[33m--注册成功--\033[0m')
        if user_status ==True:
            #path1 = os.path.abspath('..')
            #print(path1)
            file_path = os.path.join(path1, 'db', 'userup_db')
            #f = open(file_path, 'w', encoding='utf-8')
            with open(file_path,'w', encoding='utf-8') as write_file:
                #write_file.write('#_*_coding:utf-8_*_' + '\n')
                #write_file.write('import json' + '\n')
                write_file.write(json.dumps(logins))
                write_file.close()
                break