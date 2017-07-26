#_*_coding:UTF-8_*_
import os,sys,json,time,random
#
# pathdir = os.path.abspath('..')
# file_path = os.path.join(pathdir, 'status', 'typle')
# # f = open(file_path, 'r', encoding='utf-8')
# # data=json.load(f)
# # print(data)
# # if data == 'True':
# #     print('yes!')
# # else:
# #     print('no')
# # time=time.strftime('%m_%d-%H-%M')
# # print(time)
# UPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path1 = os.path.abspath('..')
# print(path1)
# print(UPDIR)
# print(sys.path.append(UPDIR))
#uid=random.randint(20,40)
#print(6024+uid)

import uuid
import os
# @uuid.uid
# def ceshi():
#     pathdir = os.path.abspath('..')
#     file_path = os.path.join(pathdir, 'db', 'iddb')
#     if os.path.exists(file_path):
#         f = open(file_path, 'r', encoding='utf-8')
#         for i in f.readlines():
#              print(i)
#
# ceshi()

import json
path1 = os.path.abspath('..')
file_path = os.path.join(path1, 'db', 'shoping_db')
f=open('shoping_db','r',encoding='utf-8')
f1 = open(file_path, 'r+', encoding='utf-8')
#while True:
for i in f:
    if i == 0:
        print('\033[32m您未购物,无需还款\033[0m')
    else:
        print('\033[32m您的清单\033[0m  %s' %(i))
        print('\033[31m----------------\033[0m')
        data=json.loads(i)
        lens=len(data)
        lens=str(data)
        print(type(lens))
        print('\033[32m您的余额%s\033[0m' % (data['hilts']))
        for j in lens:
            money = input('还款>>').strip()
            if money.isdigit():
                money = int(money)
                if money > 0 and money < 1000:
                    newmoney = money + data['hilts']
                    data['hilts'] = newmoney
                    print('\033[35m新的账单已经更新\033[0m %s' %(data))
                    f1.write(json.dumps(data) + '\n')
                    print('\033[36m<--下个订单-->\033[0m')
                    break
                else:
                    print('Nonsupport!!!')
            if money == 'q':
                exit()


