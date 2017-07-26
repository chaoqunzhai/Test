user_status = False

def login(func):        #把要执行的模块从这里传进来
    def fell():
        _username = 'zcq'
        _password= '123456'
        global user_status
        if user_status == False:
            username = input("user:")
            password = input("password:")
            if username == _username and password == _password:
                print('welcome login ...')
                user_status =True
            else:
                print('密码输入错误')
        if user_status == True:
            func()          #只要认证通过了就调用相应功能
    return fell
def home():
    print('------首页-----')
@login
def america():
    if user_status ==True:
        print('------美国-----')
@login
def japan():
    print('------日本-----')
def henan():
    print('------河南-----')
home()
#america=login(america)
america()
japan()
