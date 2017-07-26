from django.shortcuts import render,HttpResponse
from webqq.models import QQgroup
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from webqq.Msq_queue import MsgHandler
import json
# Create your views here.

@login_required    ##验证是否已经登陆
def dashboard(request):
    print("group--", QQgroup.objects.values('name'))
    QQgroups = QQgroup.objects.values('name')
    return render(request,"webqq/dashboard.html",{'QQgroups':QQgroups})
'''
from django.views.decorators.csrf import csrf_exempt 导入这个模块意思是：指定视图不进行csrf的认证
需要在视图中添加装饰器:#@csrf_exempt
'''

MSG_QUEUES = {}
# @csrf_exempt
def msg_api(request):
    '''把前端的数据提交过来，并交给MsgHandler这个模块去做对应的处理'''
    msg_obj = MsgHandler(request, MSG_QUEUES)
    print("MSG_QUEUE",MSG_QUEUES,)

    if request.method == "POST":
        msg_obj.msg_send()
        return HttpResponse(json.dumps({"msg_send_status": 1}))
    else:
        msg_data = msg_obj.msg_recv()
        return HttpResponse(json.dumps(msg_data))
