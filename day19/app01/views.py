from django.shortcuts import render
from django.shortcuts import redirect
from app01 import models
# Create your views here.


def servers(request):
    v =request.session.get('username')
    # v =request.COOKIES.get('username')
    print('vvv',v)
    if not v:
        print('111')
        return redirect('/login')

    server_list = models.UserInfo.objects.all()     #规定写法，意思是获取所有的数据

    return render(request,'servers.html',{'data':server_list})

def add_user(request):
    if request.method == 'GET':      #跳转到这个函数的时候。应该配置写了add_user的html。所有是get方法。下载的方式显示出来
        return render(request,'add_user.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        a = request.POST.get('port')

        models.UserInfo.objects.create(hostname=u,passwd=p,port=a)

        return redirect('/servers')
def del_user(request):
    uuid = request.GET.get('uid')      #这里是get html上传过来的nid对面的值
    models.UserInfo.objects.filter(uid=uuid).delete()         #删除

    return redirect('/servers')

def update_user(request):
    if request.method == 'GET':
        uuid = request.GET.get('uid')          #获取用户编辑的uid值
        v = models.UserInfo.objects.filter(uid=uuid).first()       #通过uid的值。去数据库中查看值。并返回给html中
        return render(request,'update_user.html',{'data':v})
    elif request.method =='POST':
        ##这里request.POST.get的值是。前端页面给返回的name的值
        uuid = request.POST.get('uuid')

        u = request.POST.get('user')
        p = request.POST.get('pwd')
        a =request.POST.get('port')

        models.UserInfo.objects.filter(uid=uuid).update(hostname =u,passwd=p,port=a)

        return redirect('/servers')
def update_user_new(request,nnid):       #因为urls中配置的动态url，views接受了2个参数
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(uid=nnid).first()
        return render(request,'update_user_new.html',{'data':obj})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        a =request.POST.get('port')
        models.UserInfo.objects.filter(uid=nnid).update(hostname=u,passwd=p,port=a)

        return redirect('/servers')

def groups(request):
    return render(request,'groups.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # models.UserInfo.objects.filter(username=u,pwd=p).count()
        obj = models.UserInfo.objects.filter(hostname=u, passwd=p).first()
        if obj:
            obj = redirect('/servers')
            # 在请求者的口袋放东西
            # import datetime
            # d = datetime.datetime.utcnow()
            # m = datetime.timedelta(seconds=10)
            # end = d + m
            # obj.set_cookie(key='user_name',value=u,max_age=10,expires=end)
            # obj.set_cookie(key='username', value=u, max_age=10)
            request.session['username'] = u
            return obj
        else:
            return render(request, 'login.html', {'msg': '用户或密码错误'})
