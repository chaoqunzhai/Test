class Persion(object):          #新式类写法
    '''学习成员属性父类'''
    member = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()          #这里也可以这样写，可以直接调用enroll函数

    def enroll(self):
        '''注册'''
        Persion.member += 1
        print('欢迎注册%s成功' % self.name)
    def tell(self):
        print('------info----%s' % self.name)
       # print(self.__dict__)
        for i,j in self.__dict__.items():
            print(i,j)
        print('------end----')
class Techer(Persion):

    def __init__(self,name,age,sex,salary,course):      #先继承，在重构，这里加了salary,course 2个属性
        #Persion.__init__(self,name,age,sex)   旧式类写法
        super(Techer,self).__init__(name,age,sex)  #新式类写法
        self.salary = salary
        self.course = course
    def techering(self):
        print('注册老师为%s，讲解课程为%s' %(self.name,self.course))

class Student(Persion):
    def __init__(self,name,age,sex,course,tutian):       #先继承，在重构，这里加了,course,tutian2个属性
        #Persion.__init__(self,name,age,sex) 旧式类的写法
        super(Student,self).__init__(name,age,sex)          #新式类的写法
        self.course = course
        self.tutian = tutian
    def studenting(self):
        print('注册学生%s,课程%s，学费%s' %(self.name,self.tutian,self.course))
        Persion.member += 1


t1=Techer('alex','25','F','1000000','Python')
t2=Student('翟超群','24','F','Python','10001')
# ---------- 因为子类调用的父类 所以用父类中的tell 函数执行出结果
t1.tell()
t2.tell()
t1.techering()