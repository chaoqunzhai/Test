# 1.1.2.3.5.8.13.21
# 不存值   next 只负责打印
def fel(num):
    count = 0 # 代表循环的次数ew  如果不设 将会一直循环下去
   # a = 0
   # b = 1
    a,b = 0 ,1
    while count < num:
        tmp = a
        a = b
        b = a + tmp
        count += 1
        yield a
        #print(b)
f=fel(10)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print('干点别的事情')
# print(f.__next__())
# print(f.__next__())


a=f.__next__()
print(a)
