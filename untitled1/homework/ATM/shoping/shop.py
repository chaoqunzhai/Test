#!_*_coding:utf-8_*_
import json
import os
import sys


UPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(UPDIR)
from status import typles



shop=[]
shops=[]
pice=[]
shoplist=[
    ["iphone6",5800],
    ["Macpro",12800],
    ["ipad3",2400],
    ["iphon7P",7000],
    ["Pen",20]
]


@typles.ty
def list():
    print('\033[32m温馨提示 按q就退出，购物后按y退出即时结账\033[0m')
    hilt = 15000
    path1 = os.path.abspath('..')
    while True:
        for i, j in enumerate(shoplist):
            print(i, j)
        file_path = os.path.join(path1, 'db', 'shoping_db')
        db_path = os.path.join(path1, 'db', 'userup_db')
        if os.path.exists(file_path):
            f1 = open(file_path, 'w', encoding='utf-8')
            print('\033[31m可查看购物清单,按q就退出，购物后按y退出即时结账\033[0m')
        else:
            print('\033[32m欢迎新用户\033[0m')
            f1 = open(file_path, 'w', encoding='utf-8')
        if os.path.exists(db_path) or os.path.exists(file_path):
            f2 = open(db_path, 'r', encoding='utf-8')
            auser = input('请输入编号>>').strip()
            if auser.isdigit():
                auser=int(auser)
                if auser < len(shoplist) and auser >= 0:
                    buser=shoplist[auser]
                    if buser[1] <= hilt:
                        hilt -= buser[1]
                        print(hilt)
                        shop.append(buser)
                        shops.append(buser[0])
                        pice.append(buser[1])
                        hilt=hilt-buser[1]
                        print('您购买了\033[31m%s\033[0m,您的信用余额还有 \033[41m%s\033[0m ' % (buser, hilt))
                        print('购物车%s' %shop[0])
                    else:
                        print('\033[32m您额度只有%sRMB!不足以购物商品，\033[0m' %(hilt) )
            elif auser == 'y':
                shops.sort()
                s=set(shops)
                for item in s:
                    print('\033[33m====消费记录====\033[0m')
                    print(" 产品%s   个数%d" % (item, shops.count(item)))
                    print('\033[33m===============\033[0m')
                    sum = 0
                    for i in pice:
                        sum += i
                        tag = {'number': item, 'pro': shops.count(item), 'total': sum, 'hilts': hilt}
                        f1.write(json.dumps(tag) + '\n')
                        print('\033[32m成功录入系统\033[0m')
                        break
                print("您总计消费：\033[32m % s\033[0m余额:\033[32m % s\033[0m" % (sum, hilt))
                #f1 = open(file_path, 'w', encoding='utf-8')
                #tag = {'number': item, 'pro': shops.count(item),'total':sum,'hilts':hilt}
                #f1.write(json.dumps(tag) + '\n')
                #print('\033[32m成功录入系统\033[0m')
                break
            elif auser == 'q':
                break
            else:
                break
        else:
            print('\033[31m请注册!!!!!!!!\033[0m')
            break