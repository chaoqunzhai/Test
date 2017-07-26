#这里模拟为调用主程序

from contro import account
action = input('>>')

if (hasattr(account,action)):
    func = getattr(account,action)
    result = func()
else:
    result = '404'
print(result)