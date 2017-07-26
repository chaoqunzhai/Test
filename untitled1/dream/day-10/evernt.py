import threading,time

def ligher():
    count = 0
    while True:
        if count < 30:
            if not event.is_set():
                event.set()
            print('\033[32;1m 蓝灯 \033[0m')
        elif count <34:
            print('\033[33;1m 黄灯 \033[0m')
        elif count <60:
            if event.is_set():    #
                event.clear()
            print('\033[31;1m 红灯\033[0m')
        else:
            count =0
        count +=1
        time.sleep(0.2)


def car(n):
    count = 0
    while True:
        event.wait()  #等待标志位
        print('开着特斯拉---> %s ' %n)
        count += 1
        time.sleep(0.2)

event = threading.Event()
t=threading.Thread(target=ligher)
t.start()
t2=threading.Thread(target=car,args=(1,))
t2.start()