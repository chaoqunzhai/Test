

user_status = False  # 用户登录了就把这个改成True

def login(auth_type):  # 把要执行的模块从这里传进来
    def outer(func):
        def inner(*args,**kwargs):
            print("-->",func,auth_type,args,kwargs)
            if auth_type == "qq":
                _username = "zcq"  # 假装这是DB里存的用户信息
                _password = "123"  # 假装这是DB里存的用户信息
                global user_status
                if user_status == False:
                    username = input("user:")
                    password = input("pasword:")
                    if username == _username and password == _password:
                        print("welcome login....")
                        user_status = True
                    else:
                        print("wrong username or password!")
                if user_status == True:
                    func(*args,**kwargs)  # 看这里看这里，只要验证通过了，就调用相应功能
            else:
                print("only support qq...")
        return inner
    return outer

def pay_check():
    print('pay')