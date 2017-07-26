import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

DB_DIR='%s\DB' %BASE_DIR
DB_list=os.listdir(DB_DIR)



DB_APPKEY=r'%s\core\Appkey' %BASE_DIR
B2C_USER=r'%s\core\b2cuser' %BASE_DIR
DB_CSV=r'%s\core\b2c.csv' %BASE_DIR
DB_HOST='192.168.29.11'
DB_NAME='b2cplus'
DB_USER='palmb2c'
DB_PASSWD='palmb2c'
conn_sql='SELECT appkey,REMARK from appkey;'