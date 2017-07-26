import time

def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        x = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time %s secs."%(func.__name__, t2-t1))
        return x
    return wrapper

@cal_time
def bin_search(data_set, val):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return

@cal_time
def sys_search(data_set, val):
    try:
        return data_set.index(val)
    except ValueError:
        return
@cal_time
def in_search(data_set, val):
    return val in data_set

data=list(range(1,100000000))
num=999999
bin_search(data,num)
sys_search(data,num)
in_search(data,num)
