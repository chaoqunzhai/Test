import re
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def dive(x,y):
    return x / y
def powers(x,y):
    return pow(x,y)
def nbcla():
    return
if __name__ == '__main__':
    function='''\033[35m
    1:加法
    2:减法
    3:乘法
    4:除法
    5:次方
    \033[0m
    '''
    function_dic={
        '1':add,
        '2':sub,
        '3':mul,
        '4':dive,
        '5':powers,
    }

    while True:
        print(function)
        choice = input('请选择计算>>>').strip()
        if choice == 'q': break
        if len(choice) == 0 or choice not in function_dic: continue
        num1=int(input("输入第一个数字: "))
        num2=int(input("输入第二个数字: "))
        print('\033[35m计算得出结果》》》\033[0m \033[36m%s ！！！\033[0m'%(function_dic[choice](num1,num2)))

