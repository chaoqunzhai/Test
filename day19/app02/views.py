from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import os
def test(request):
    return HttpResponse('app02--test')

def upload(request):
    if request.method == 'GET':
        return render(request,'upload.html')
    elif request.method == 'POST':
        obj = request.FILES.get('new_file')
        with open(os.path.join('upload',obj.name),'wb') as f:
            for line in obj.chunks():         #chunks() 是一个迭代器，，obj.name是这个文件的名称
                f.write(line)

        return HttpResponse('提交成功')
