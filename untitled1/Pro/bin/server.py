import os
import sys
import pymysql
import csv
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import main
from conf import file_path


class Hander(object):
    def __init__(self,username,number,userid):
        self.username=username
        self.number=number
        self.userid=userid
        self.file()
        self.connct_mysql()
        file_path.file_rename()
    def connct_mysql(self):
        try:
            self.conn = pymysql.connect(host=main.DB_HOST,
                                        port=3306,
                                        user=main.DB_USER,
                                        passwd=main.DB_PASSWD, db=main.DB_NAME,charset='utf8')
            self.cursor = self.conn.cursor()
            self.conn_sql=main.conn_sql
            self.db_sql(self.conn_sql)
            self.conn_close()
        except TimeoutError as e:print('连接超时')
        except pymysql.err.OperationalError as q:print('连接中断')
    def conn_close(self):
        self.cursor.close()
        self.conn.close()
    def file(self):
        self.DB_number=len(main.DB_list)
        if self.DB_number==0:exit()
        self.DBfile_number=0
        conn = 0
        for i in main.DB_list:
            self.DB_list2 = '%s\%s' % (main.DB_DIR, i)
            self.DB_file=os.listdir(self.DB_list2)
            if len(self.DB_file) > self.DBfile_number:
                for e in range(len(self.DB_file)):
                    conn +=1
                    #print('file:文件目录%s,文件%s,个数为%s'%(i,self.DB_file[e],conn))
                    self.file_all='%s\%s' %(self.DB_list2,self.DB_file[e])
                    self.open_file(self.file_all,conn)
    def open_file(self,file_all,conn):
        self.filelist = {}
        self.filelist[conn]=file_all
        count = 0
        for v in self.filelist:
            count += 1
            with open(main.DB_APPKEY,'a') as appkey,\
                    open(self.filelist.get(v),'r') as f,\
                    open(self.filelist.get(v), 'r') as e,\
                    open(main.B2C_USER,'a') as b2c_user:
                while True:
                    line=f.readlines()
                    for j,x in enumerate(line):
                        j +=1
                        print('目录:%s，当前文件为:%s,文件行数:%s,APPKKEY:%s,用户:%s,访问目录:%s'
                                  %(self.filelist.get(v).split('\\')[-2],
                                    self.filelist.get(v).split('\\')[-1],
                                    j, x.split(',')[2],x.split(',')[3],x.split(',')[5]))
                        appkey.write(x.split(',')[2]+'\n')
                        b2c_user.write(x.split(',')[2]+'-'+x.split(',')[3]+'\n')
                    if not line:break
    def b2c_user(self,row):
        with open(main.B2C_USER) as e:
            line=e.readlines()
            line=list(set(line))
            klist=[]
            dict01={}
            dict02 = {}
            for i in line:
                for k, v in enumerate(row):
                    (appkey,user)=(i.split('-')[0],i.split('-')[1])
                    #print('appkey,user',appkey,user)
                    if appkey == v[0]:
                        klist.append(k)
                        print('K:%s,APPKEY:%s,UserID:%s,'%(k,appkey,user))
                        break
            setklist=set(klist)
            for i in setklist:
                dict01.update({i:klist.count(i)})
                #dict02.update({i: str(klist.count(i)) +'-'+ row[i][1]})
                dict02.update({row[i][1]:str(klist.count(i))})
            return dict02
    def db_sql(self, conn_sql):
        self.DB_dict = {}
        results={}
        self.a=''
        self.cursor.execute(conn_sql)
        row = self.cursor.fetchall()
        if os.path.isfile(main.DB_APPKEY):
            with open(main.DB_APPKEY) as f:
                line = f.readlines()
                self.a=self.b2c_user(row)
                for k, v in enumerate(row):
                    v = list(v)
                    self.DB_dict[v[1]] = v[0]
                    for i in line:
                        if self.DB_dict[v[1]] in i:
                            number= line.count(i)
                            #print(v[1],self.DB_dict[v[1]],number)
                            results[v[1]]=[self.DB_dict[v[1]],number]
                            break
        if results is not None:self.csv_handle(results,row,self.DB_dict)
    def csv_handle(self,result,row,db_dict):
        ceshi = self.a
        notuser={}
        with open(main.DB_CSV, mode='w', newline='') as f:
            headers = [self.username, self.number, self.userid]
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            for i,k in enumerate(result):
                for line in ceshi:
                    if line == k:
                        #print(i,k,result[k][0],result[k][1],ceshi[line])    ##wirte csv
                        del db_dict[k]
                        notuser.update({k:{result[k][1]:ceshi[line]}})
            for i in db_dict:
                notuser.update({i:{0:'0'}})
            print(notuser)
            for l in notuser:
                for k in notuser[l]:
                    #print(l,k, notuser[l][k])
                    rok=[{self.username:l,
                              self.number:k,
                              self.userid:notuser[l][k]}]
                    writer.writerows(rok)

if __name__ == '__main__':
    Hander('客户名称', '访问次数', '访问客户')







