class Persion(object):
    '''描述方法'''
    def __init__(self,name):
        self.name = name
        #self.__status = None
    def check_status(self):
        print('航班状态  %s' %(self.name))
        return 1
    @property
    def flight_status(self):
        status = self.check_status()
        if status == 0:
            print('0000')
        elif status == 1:
            print('状态为1')
        else:
            print('----------------')
    @flight_status.setter
    def flight_status(self,status):
        self.__status = status
        print('用setter装饰器修改flight_status返回值')
        print('self_status值为:',self.__status)

    def __call__(self, *args, **kwargs):
        print("__call",args,kwargs)
    def __str__(self):
        return '<fligh:%s,status:%s>' %(self.flight_status,self.__status)
    def __getitem__(self, item):
        print('get item',item)
        return 22
    def __setitem__(self, key, value):
        print('set key',key,value)
    def __delitem__(self, key):
        print('dele ',key)

f=Persion('AC98')
print(f.__module__)       #__main__
print('_doc_',f.__doc__)      #打印注释
f.flight_status           #
f.flight_status =10       #因为@property 是把一个方法变成一个静态属性所以这也就可以理解为变量的赋值   这段赋值是因为下面又写了个flight_status 函数 这函数用了装饰器@flight_status.setter
                       # 就会打印这函数下定义的值


result = f['k1']
f['k2'] = 'zcq'
print(f['age'])
#print(f[])