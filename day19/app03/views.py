from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse('app03--test')
def tpl(request):
    return render(request,'tpl.html',{'data':'如果没有梦想，那跟咸鱼还有什么区别'})
