
from greenlet import greenlet

def test1():
    print('test1:我是1')
    gr2.switch()    #切换到test2
    print('test1:我是1.1')
    gr2.switch()
def test2():
    print('test2:我是2')
    gr1.switch()  #切换到test1
    print('test2:我是2.2')


gr1=greenlet(test1)
gr2=greenlet(test2)
gr1.switch()      #先切换到test1