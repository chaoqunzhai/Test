import gevent


def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(0.5)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    #threads = [gevent.spawn(task, i) for i in range(10)]
    threads=[]
    for i in range(10):
        threads.append(gevent.spawn(task,i))
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
