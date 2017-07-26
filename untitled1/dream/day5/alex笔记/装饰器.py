# _*_coding:utf-8_*_

import auth
from auth import login
from auth import *

def pay_check():
    print("hahah ")

pay_check()


def home():
    print("---首页----")
@login("qq")
def america():
    # login() #执行前加上验证
    print("----欧美专区----")

@login('weixin')
def japan():
    print("----日韩专区----")


def henan(style):
    # login() #执行前加上验证
    print("----河南专区----",style)


home()
#america = login(america)  #inner  需要验证就调用 login，把需要验证的功能 当做一个参数传给login
print(america)
# home()


america() #inner()
henan = login(henan) #inner
print('==================')
japan()
# henan("4p") #inner(4p)

