from django.shortcuts import render
from  bbs import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from bbs import forms
# Create your views here.


def index(request):


    categories = models.Category.objects.filter(set_as_top_menu=True)
    return render(request,'index.html', {"categories":categories})


def category(request,category_id):
    categories = models.Category.objects.filter(set_as_top_menu=True)


    articles = models.Article.objects.filter(category_id=category_id)

    paginator = Paginator(articles, 5)  # Show 25 contacts per page

    # page = request.GET.get('page')
    # try:
    #     objs = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     objs = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     objs = paginator.page(paginator.num_pages)

    return render(request,'index.html', {"categories":categories, "articles":articles})


def article_detail(request,article_id):

    article_obj = models.Article.objects.get(id=article_id)


    return  render(request,"article.html",{"article":article_obj})


def new_article(request):

    if request.method == "POST":
        print("request post:",request.POST)
        print("request files:",request.FILES,request.user )


        article_form = forms.ArticleForm(data=request.POST,files=request.FILES)
        if article_form.is_valid():
            print("formdata", article_form.cleaned_data)
            # article_form.cleaned_data['author_id'] = request.user.id
            # # #article_form.save()
            # # obj = models.Article(**article_form.cleaned_data)
            # # obj.save()
    else:

        article_form = forms.ArticleForm()

    return  render(request,"new_article.html",{"form":article_form})
