import gevent

def func1():
    print('\033[31;1m我是func1\033[0m')
    gevent.sleep(3)
    print('\033[31;1m我是func1.1--我上面有3秒\033[0m')

def func2():
    print('\033[32;1m我是func2.\033[0m')
    gevent.sleep(2)
    print('\033[32;1m我是func2.1 我上面有2秒\033[0m')

def func3():
    print('\033[32;1m我是func3.\033[0m')
    gevent.sleep(2)
    print('\033[32;1m我是func3.1我上面有2秒\033[0m')

gevent.joinall([gevent.spawn(func1),
                gevent.spawn(func2),
                gevent.spawn(func3),])