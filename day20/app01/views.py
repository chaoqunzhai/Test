from django.shortcuts import render,HttpResponse
from django.views import View

from app01.forms import MailSendForm,BootForm

# Create your views here.


def email(request):
    if request.method == "POST":
        form = MailSendForm(request.POST) #把前端post过来的数据交给这个类去验证
        if form.is_valid(): #form.is_valid 验证表单是否合法
            print("going to send mail....",form.cleaned_data)
            '''
            form.cleaned_data 就是把前端提交过来的数据，进行一定的清洗 ，也就是清洗过后的数据
            例如:前端写的是数字，但是发到后端的还是字符串，后端就会尝试把字符串转成数字
            '''
        else:
            print("error happend during validation:",form.errors)
    else:
        form=MailSendForm(initial={'sender':'翟超群@qq.com','content':'这些都是自定义'})
    return render(request, 'email.html', {'form': form})

def book_mgr(request):
    if request.method == "POST":
        form =BootForm(data=request.POST)
        if form.is_valid():
            form.save()
            form=BootForm()
    else:
        form=BootForm()

    return render(request,'book.html',{'form':form})

class BookMgr(View):

    from_class = BootForm
    template_name = 'book.html'

    def get(self,request):
        print('get',request.GET)
        form =self.from_class()

        return render(request,self.template_name,{'from':form})
    def post(self,request):
        form = self.from_class(data=request.POST)
        if form.is_valid():
            form.save()
            form =self.from_class()
        return render(request,self.template_name,{'form':form})

