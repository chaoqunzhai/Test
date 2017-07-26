
class Persion(object):
    def __init__(self,name,age):
        self.name =name
        self.age = age
        self.sex = 'noraml'
    def talk(self):
        print('调用talk函数  person is talking ......')

class BlackPerson(Persion):

    def __init__(self,name,age,strength): #先继承，在重构   继承父类的时候 ，如果父类有构造函数，子类也必须有 所以这里写了__init__
        self.strength = strength          # 继承父类后，子类也添加构造函数，如果新增功能，子类也必须在self.新方法
        Persion.__init__(self,name,age)
        print(self.name,self.age,self.sex,self.strength)
    def tal(self):
        print('调用父类中的talk函数' )
        Persion.talk(self.name)           #父类.方法
    def walk(self):
        print('is walking......')
b=BlackPerson('翟超群','24','good')    #因为调用父类  父类中有构造函数，所以必须穿参
b.tal()
b.walk()