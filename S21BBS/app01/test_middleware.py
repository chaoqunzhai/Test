from django.shortcuts import HttpResponse


#钩子middleware方法！
#在setting中添加配置，相当于全局都需要过这个middeware插件

class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print("middleware",response)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    #捕用户访问view的时候，就会先经过这里，然后才去调用view视图函数，所以这里可以拿到很多信息
    def process_view(self,request,view_func,view_args,view_kwargs):

        print("process_view",self,request,view_func,view_args,view_kwargs)
        # if request.META.get("REMOTE_ADDR") == "127.0.0.1":
        #     return HttpResponse("拒绝本地访问")

    #如果view里面出现了错误，就会定位到这里，可以做自定制的错误页面
    def process_exception(self,request,exception):
        print("proces exception",request,exception)

        return HttpResponse("<h1>您访问的页面%s不存在！错误信息:%s,%s</h1>" %(exception,request,exception))
    # def process_template_respone(self,request,response):
    #     print("process_template",request,response)