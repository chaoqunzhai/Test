import time
def xiaofei(name):
    print('准备吃包子')
    while True:
        baozi=yield
        print('包子%s来了，被%s吃掉' %(baozi,name))
def chushi(name):
    a=xiaofei('A')
    b=xiaofei('B')
    a.__next__()
    b.__next__()
    print('开始做包子')
    for i in range(10):
        time.sleep(1)
        print('做了2个包子')
        a.send(i)
        b.send(i)
chushi('')
