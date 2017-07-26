class Dog(object):
    member = 100            #公有属性
    def __init__(self,name,age):      # 构造函数
        self.NAME =name               #构造函数属性
        self.AGE = age
        self._heart = 'yes'
    def sayhai(self):
        print('my name is %s , age is %s' %(self.NAME,self.AGE))
        self._heart = 'no'          #修改私有属性
        print('状态 %s' %self._heart)
    def b_heart(self):
        return self._heart          #外部调用接口查询私有属性

    def eat(self,food):
        print('%s    is eating    状态%s    %s' %(self.NAME,self._heart,food))
    def __del__(self):           #析构函数
        print('del..........')


d=Dog('dahong','5')   #实例化
d2=Dog('xiaoming','30')  #实例化
print('访问__init__的name属性:',d.NAME)
d.NAME='zcq'        #修改构造函数属性
print('查询修改构造函数的属性:',d.NAME)
print('打印私有属性:',d.b_heart())

d.sayhai()       #实例
print(d.b_heart())
d2.sayhai()    #实例
d2.eat('banna')          #传入eat定义的food对应的值
print(d.member)           # 打印公有属性
Dog.member = 20           #修改公有属性
print('第一个实例化的私有属性',d.member)
print('弟二个实例化的私有属性',d2.member)
