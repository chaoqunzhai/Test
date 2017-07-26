
def say():
    username = input("请输入您的用户名:")
    password = input("请输入密码")
    _username='zcq'
    _password='123456'
    if username == _username and password == _password:
        print('\033[34m欢迎您登陆成功\033[0m')
        return True
def home():
    if say() == True:
        print("\033[32m登录成功，进入您的home\033[0m")
        return True
    else:
        print('\033[33m请您重新输入\033[0m')
        say()
def pay():
    if home() == True:
        print("\033[35m欢迎进去您的购物车\033[0m")
    else:
        say()
#pay()
