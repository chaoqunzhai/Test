import os
import sys
import time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import main

new=os.path.join(BASE_DIR,main.DB_APPKEY.split('\\')[-2])

file_time=time.strftime('%m-%d-%M-%S')

def file_rename():
    os.chdir(new)
    def path():
        if os.path.isfile(main.DB_APPKEY):
                file_appkey = main.DB_APPKEY.split('\\')[-1]
                os.rename(main.DB_APPKEY, file_appkey + file_time)
        if os.path.isfile(main.B2C_USER):
            file_user = main.B2C_USER.split('\\')[-1]
            os.rename(main.B2C_USER, file_user + file_time)
    path()
#file_rename()