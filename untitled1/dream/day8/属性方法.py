class Perison(object):
    name = '我是类变量，我在顶部'
    def __init__(self,name):
        self.name = name

    @staticmethod        #静态方法：既不能访问公有属性，也不能访问实例属性
    def eat(name,food):
        print("静态方法 %s %s" %(name,food))

    @classmethod   # 类方法:只能访问类的公有属性，不能访问实例属性
    def walk(self):
        print("类方法",self.name)

    @property        #属性方法的作用把一个方法变成一个静态属性（也就是把方法变成一个变量）
    def talk(self):
        print("属性方法 %s" %self.name)



a= Perison('zcq')
a.eat('rch','apple')
a.walk()
a.talk