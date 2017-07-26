# -*- coding: utf-8 -*-
import pickle
import os
import sys
UPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(UPDIR)

class Persion(object):
    all_teacher = 0
    all_student = 0
    def __init__(self,name,city,school):
        self.name = name
        self.city = city
        self.school = school
    def all_t(self):
        Persion.all_teacher +=1
    def all_s(self):
        Persion.all_student +=1
class Admin(Persion):
    def __init__(self,name,city,school,banji,courses):
        super(Admin,self).__init__(name,city,school)
        self.banji = banji
        self.courses = courses
    def main(self):
        while True:
            username = 'zcq'
            userpassword = '123'
            user_name = input('请输入用户名[zcq]>').strip()
            user_password = input('请输入密码[123]>').strip()
            if user_name == 'q' or user_password == 'q':break
            if user_name == username and user_password == userpassword :
                print('\033[1;35m登录成功\033[0m')
                banji_input = input(' 输入要创建班级名称>>').strip()
                name_input = input('输入班级老师>>').strip()
                couruse_input = input('输入课程>>').strip()
                self.banji = banji_input
                self.name = name_input
                self.courses = couruse_input
                print('\033[1;33m 创建班级:%s，创建老师:%s, 新开课程:%s\033[0m' %(self.banji,self.name,self.courses))
                break
class City(Admin,Persion):
    def __init__(self,name,city,school,courses,banji,money,*args):  #cycles,money
        super(City,self).__init__(name,city,school,banji,courses)
        self.name = name
        self.city = city
        self.money = money
    def info(self):
        print('\033[32m===========\033[0m')
        print('老师个数%s' % Persion.all_teacher)
        print('注册成功！%s 信息如下:' % self.name)
        for i,j in self.__dict__.items():
            print(i + ':',j)
        print('\033[32m===========\033[0m')
    def db_test(self):
        with open('db','wb') as f:
             pickle.dump(self.__dict__,f)
    def db_name(self):
        if os.path.isfile(self.name):
            print('\033[34m您已经注册过该系统！！！！\033[0m')
        else:
            os.rename('db', self.name)
    def db_read(self):
        with open(self.name,'rb') as f1:
            data=pickle.loads(f1.read())
        return data
    def shanghai(self):
        if self.city == 'shanghai' or self.city =='上海':
            self.courses = 'go'
            self.cycles = '10'
            self.money = '12000'
            self.banji = '10day'
            self.school = 'dream!'
            self.db_test()
            self.db_name()
            # self.all()   self.info()  详细信息
            #print(Admin.main(self.banji))
        else:
            print('输入格式错误')
        if self.name == 'alex':
            self.all_t()
            self.info()
            print('\033[1;31m>>>>>课程老师:%s，所在城市:%s，学校名称:%s，培训课程%s\033[0m' % (self.name, self.city, self.school, self.courses))
    def beijing(self):
        if  self.city == 'beijing' or self.city == '北京':
            self.cycles = '7'
            self.money = '11000'
            self.banji = '15day'
            self.courses = 'Python|Linux'
            self.school = 'oldbay'
            self.db_test()
            self.db_name()
            # self.all()   self.info()  详细信息
        else:
            print('输入格式错误')
        if self.name == '林海峰':
            self.all_t()
            self.info()
            print('\033[1;31m>>>>>课程老师:%s，所在城市:%s，学校名称:%s，培训课程%s\033[0m' % (self.name, self.city, self.school, self.courses))
class Sign(City):
    def __init__(self,name,city,*args):
        super(Sign,self).__init__(name,city,*args)
    def db_techaer(self):
        with open('db_teacher','a+',encoding='utf-8') as fdb:
            fdb.write(self.name)
            fdb.write(':')
            fdb.write(self.banji)
            fdb.write(':')
            fdb.write(self.courses)
            fdb.write('\n')
    def db_student(self):
        with open('db_student','a+',encoding='utf-8') as fdb:
            fdb.write(self.name)
            fdb.write(':')
            fdb.write(self.banji)
            fdb.write(':')
            fdb.write(self.courses)
            fdb.write('\n')
    def sings(self):
        while True:
            choice_city = input('\033[1;31m请选择城市[<帝都|魔都>] 按q退出>>:\033[0m').strip()
            if choice_city == 'q':break
            if choice_city == 'beijing' or choice_city== '北京':
                role = input('[1:老师][2:学生]>>').strip()
                if role == 'q':break
                if role == '1':
                    name = input('请输入名字>>:').strip()
                    self.city = choice_city
                    self.name = name
                    City.beijing(self)
                    Sign.db_techaer(self)
                    print('\033[1;35m代课老师:%s，所在城市:%s，学校名称:%s，培训课程%s\033[0m' % (self.name, self.city, self.school, self.courses))
                    continue
                if role == '2':
                    name = input('请输入名字>>:').strip()
                    self.city = choice_city
                    self.name = name
                    City.beijing(self)
                    self.all_s()
                    self.info()
                    Sign.db_student(self)
                    print('班级:%s   学员数:%s' %(self.banji,Persion.all_student))
                    print('\033[1;36m学员%s,课程%s，班级%s,学费%s\33[0m' %(self.name,self.courses,self.banji,self.money))
                    continue
            if choice_city == 'shanghai' or choice_city== '上海':
                role = input('[1:老师][2:学生]>>').strip()
                if role == '1':
                    name = input('请输入名字>>:').strip()
                    self.city = choice_city
                    self.name = name
                    City.shanghai(self)
                    Sign.db_techaer(self)
                    print('\033[1;35m代课老师:%s，所在城市:%s，学校名称:%s，培训课程%s\033[0m' % (self.name, self.city, self.school, self.courses))
                    continue
                if role == '2':
                    name = input('请输入名字>>:').strip()
                    self.city = choice_city
                    self.name = name
                    City.shanghai(self)
                    self.all_s()
                    self.info()
                    Sign.db_student(self)
                    print('班级:%s  学员数%s' %(self.banji,Persion.all_student))
                    print('\033[1;36m学员%s,课程%s，班级%s,学费%s\033[0m' % (self.name, self.courses, self.banji,self.money))
                    continue
class Students(City):
    def __init__(self,name,city,*args):
        super(Students, self).__init__(name, city, *args)
    def students(self):
        students_v = input('\033[1;32m如果已经注册直接输入名字可查询>>\033[0m').strip()
        if os.path.isfile(students_v):
            self.name = students_v
            print(self.db_read())
            print('yes')
            while True:
                students_money = input('\033[1;33m输入缴费金额，无需缴费按q退出>>\033[0m').strip()
                if students_money.isdigit():
                    students_money = int(students_money)
                    date=self.db_read()
                    datenew=date['money']
                    datenew=int(datenew)
                    datenew += students_money
                    date['money'] = datenew
                    with open(self.name,'wb') as f1:
                        pickle.dump(date,f1)
                        print('\033[1;35m缴费成功，金额为%s\033[0m' %(date['money']))
                        print(date)
                if students_money == 'q':
                    break
        else:
            print('请注册！')
class Teacher(Students):
    def __init__(self,name,city,*args):
        super(Teacher, self).__init__(name,city,*args)
    def teacher(self):
        while True:
            a = input('\033[1;34m查看老师信息按T|查看学生信息按S|按q退出>>\033[0m').strip()
            if a == 'q':break
            if a == 'T' or a == 't':
                if os.path.isfile('db_teacher'):
                    with open('db_teacher',encoding='utf-8') as tfile:
                        print('\033[1;36m老师信息 ===》')
                        print('%s\033[0m' %tfile.read())
                        continue
                else:
                    print('\033[1;33m未有注册老师\033[0m')
                    continue
            if a == 'S' or a == 's':
                if os.path.isfile('db_student'):
                    with open('db_student',encoding='utf-8') as tfile:
                        print('\033[1;36m学生信息 ===》')
                        print('%s\033[0m' %tfile.read())
                        continue
                else:
                    print('\033[1;33m未有注册学员\033[0m')
if __name__ == '__main__':
     function = '''
      1:查看北京课程
      2:查看上海课程
      3:老师|学员注册
      4:学员登录查看
      5:老师登录查看
      6:选择管理员
      '''
     t1 = City('林海峰', '北京', ' ', '', '','')
     t2 = City('alex', '上海', ' ', '', '','')
     t3 = Sign('翟超群','北京 ',' ','','','')
     t4 = Students('翟超群','北京 ',' ','','','')
     t5 = Teacher('翟超群','北京 ',' ','','','')
     t6 = Admin('翟超群', '北京 ', ' ', '','')
     function_dict={
         '1':t1.beijing,
         '2':t2.shanghai,
         '3':t3.sings,
         '4':t4.students,
         '5':t5.teacher,
         '6':t6.main
     }
     while True:
          print(function)
          choice=input('选择属性>>:').strip()
          if choice == 'q':break
          if len(choice) == 0 or choice not in function_dict:continue

          function_dict[choice]()