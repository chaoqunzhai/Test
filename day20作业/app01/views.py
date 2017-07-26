from django.shortcuts import render,HttpResponse
from app01.forms import  MailSendForm


def index(request):
    return render(request,'index.html')





