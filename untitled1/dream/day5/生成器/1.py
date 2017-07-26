date=[1,2,3,4]
#列表生成器  列表生成式  ，已经在内存中生成
date=[i*2 if i >2 else i for i in date]
print(date)


#惰性算法。 求值多少给多少，不能跳着取值
date1=(x**2 for x in range(20))
print(date1)
print(date1.__next__())
print(date1.__next__())
#print(next(date1))
print(date1.__next__())
print(date1.__next__())
print(date1.__next__())
print(date1.__next__())

#print(date1.__next__())         #
# for i in date1:
#     print(i)



