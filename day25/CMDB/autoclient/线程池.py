from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time

def task(i):
    print(i)
    time.sleep(1)

pool = ThreadPoolExecutor(10)
for index in range(66):
    pool.submit(task,index)

print('end')