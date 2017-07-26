#!_*_coding:utf-8_*_
import os
import json

status=False
def ty(func):
    def mode():
        global status
        pathdir = os.path.abspath('..')
        file_path=os.path.join(pathdir,'status','typle')
        if os.path.exists(file_path):
            f=open(file_path,'r',encoding='utf-8')
            data=json.load(f)
            if data == 'True':
                status = True
                print('\033[31m《《《登录状态》》》》\033[0m')
            if status == True:
                func()
    return mode