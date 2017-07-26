#循环到999就报错
def func(n):
    #print(n)
    if n//2 > 0:
        func(n//2)
    print(n)
func(10)

