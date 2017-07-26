from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app01 import forms
from django.contrib.auth import  authenticate,logout,login
from django.contrib.auth.decorators import login_required


def index(request):
    return redirect("/category/all/")    #跳转到所有的内容
    # categories= models.Category.objects.filter(set_as_top_menu=True)         #取出set_as_top_menu=true的值
    # # print('casss-index',categories)
    # return render(request,'index.html',{'categories':categories})


def category(request,category_id):
    categories = models.Category.objects.filter(set_as_top_menu=True)
    if category_id == 'all':
        articles = models.Article.objects.all().order_by("-id")    #倒叙
    else:

        articles = models.Article.objects.filter(category_id=category_id).order_by("-id")     #根据ID过滤后的数据 然后在分页

    paginator = Paginator(articles, 2)  #分页功能  2的意思是一页分2条
    # raise 'error'
    page = request.GET.get('page')         #前端发送一个page  去url里面取page的值
    try:
        contacts = paginator.page(page)          #如果不是整理
    except PageNotAnInteger:

        contacts = paginator.page(1)
    except EmptyPage:                     #如果是空页

        contacts = paginator.page(paginator.num_pages)       #最后一页返回给用户

    return render(request,'index.html',{'categories':categories,'articles':contacts})

def article(request,article_id):

    article_obj = models.Article.objects.get(id=article_id)

    return render(request,"article.html",{"article":article_obj})


#from django.contrib.auth.decorators import login_required    判断是否已经登陆   。才可以进行发帖
#加上这个装饰器，它就会默认的自动的跳到一个    accounts/login?  的一个url里面
#如果你不想用这个accounts/login   那你就需要去你setting里面去加一段
#
#LOGIN_URL = "login"      这里写的是你login  url控制器写的内容
 #
#当你没有认证通过的时候， 试图去点这个内容，它就会自动的跳到login页面(上面你setting中配置的url)中，并且它会记录你上次点击内容例如http://127.0.0.1:8000/login?next=/new_article
#

@login_required
def new_article(request):
    #request.FILE,request.user
    print('user',request.user)
    if request.method == "POST":
        #如果前端传入了文件，那后端就需要使用request.FILES 来解释
        article_form = forms.ArticleFrom(data=request.POST,files=request.FILES,)
        if article_form.is_valid():
            article_form.cleaned_data['author_id'] = request.user.id     #在清除后的数据中添加 author，这个author是根据数据库中的字段来进行添加
            #article_form.save()
            print('user',request.user.id)
            print('clean data',article_form.cleaned_data)
            tags = article_form.cleaned_data.pop("tags")
            obj = models.Article(**article_form.cleaned_data)
            obj.save()
            obj.tags.add(*tags)
            obj.save()
            return HttpResponse('''<button type="button" class="btn btn-success" alert='yes'>（成功）Success</button>''' )
    else:

        article_form = forms.ArticleFrom()

    return render(request,'new_article.html',{"form":article_form})


def acc_login(request):
    #from django.contrib.auth import  authenticate  导入这个模块 django 自带了用户检测
    errors = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        #这一句话只是做了认证
        user = authenticate(username=username,password=password)# 如果用户验证成功了。就会返回用户对象
        if user:
            print("验证成功")
            ##from django.contrib.auth import  authenticate,logout,login
            login(request,user)      #此时你才登陆成功
            #你没有认证通过的时候， 试图去点加了装饰器认证后的内容，
            # 它就会自动的跳到login页面(上面你setting中配置的url)中，并且它会记录你上次点击内容例如http://127.0.0.1:8000/login?next=/new_article
            #如果用户通过了认证，那就返回到用户点击上次的地方，
            #其中url中 next后面就是上次点击的地方，直接get就行
            return redirect(request.GET.get("next") or "/")
        else:
            errors = {"error":"用户名或者密码错误"}
            print(errors)
    return  render(request,'login.html',errors)

def acc_logout(request):
#from django.contrib.auth import  authenticate,logout  导入
    logout(request)

    return redirect("/login")