#_*_coding:UTF-8_*_
import os
import sys
import time
import json
UPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(UPDIR)

from status import register
from status import userin
from shoping import shop
from status import typles

time=time.strftime('%m_%d-%H-%M')
user_status = False

def singnup():
    register.userup()

@userin.login
def singnin():
    return 'yes'

def shopping():
    shop.list()

@typles.ty
def giro():
    print('\033[32m正在开发的路上\033[0m')

@typles.ty
def payments():           #这里不知道为什么有一个小bug，在用户生成购物清单后，在这执行还款，就会在文件后面写一个 ‘800}’ 这样的东东。
    path1 = os.path.abspath('..')
    file_path = os.path.join(path1, 'db', 'shoping_db')
    f = open(file_path, 'r', encoding='utf-8')
    f1 = open(file_path, 'r+', encoding='utf-8')
    for i in f:
        if i == 0:
            print('\033[32m您未购物,无需还款\033[0m')
        else:
            print('\033[32m您的清单\033[0m  %s' % (i))
            print('\033[31m----------------\033[0m')
            data = json.loads(i)
            lens = len(data)
            lens = str(data)
            print(type(lens))
            print('\033[32m您的余额%s\033[0m' % (data['hilts']))
            for j in lens:
                money = input('还款>>').strip()
                if money.isdigit():
                    money = int(money)
                    if money > 0 and money < 100000:
                        newmoney = money + data['hilts']
                        data['hilts'] = newmoney
                        print('\033[35m新的账单已经更新\033[0m %s' % (data))
                        f1.write(json.dumps(data) + '\n')
                        print('\033[36m<--下个订单-->\033[0m')
                        break
                    else:
                        print('Nonsupport!!!')
                if money == 'q':
                    break
@typles.ty
def getmoney():
    print('\033[32m正在开发的路上\033[0m')

def exit():
    pathdir = os.path.abspath('..')
    file_path = os.path.join(pathdir, 'status', 'typle')
    if os.path.exists(file_path):
        os.rename(file_path,file_path+time)

if __name__ == '__main__':
    function='''\033[35m
        1:注册
        2:登录
        3:购物
        4:转账
        5:还款
        6:取现
        7:<退出请按‘q’，清空历史记录请按‘7’>
        \033[0m'''
    function_dict={
        '1':singnup,
        '2':singnin,
        '3':shopping,
        '4':giro,
        '5':payments,
        '6':getmoney,
        '7':exit
    }
    while True:
        print(function)
        choice=input('请选择模块>>').strip()
        if choice == 'exit'or choice == 'q':break
        if len(choice) == 0 or choice not in function_dict:continue

        function_dict[choice]()

