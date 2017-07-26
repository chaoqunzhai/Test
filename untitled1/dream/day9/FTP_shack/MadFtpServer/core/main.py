import optparse
from core.ftp_server import FTPHandler
from conf import settings



import socketserver
class ArvgHandler(object):
    def __init__(self):
        self.parser = optparse.OptionParser()
        self.parser.add_option("-z", '--start!', dest="server", help="启动服务")
        self.parser.add_option("-s",'--host',dest="host",help="绑定server ip")
        self.parser.add_option("-p", '--port', dest="port", help="绑定server 端口")
        (options, args) = self.parser.parse_args()
        # print("parser",options,args)
        # print(options.host,options.port)
        self.verify_args(options,args)
    def verify_args(self,options,args):
        try:
            if hasattr(self,args[0]):        #使用反射来判别参数
                func = getattr(self,args[0])
                func()          #得到这个参数去调用 例如如果得到参数args[0] == start ,那这里func()。也就是start()  。就会调用下面的函数
            else:
                self.parser.print_help()
        except IndexError as e:
            print('---后面必须跟参数----详情<-h>可查看')
    def start(self):
        print('----server start----')
        server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), FTPHandler)
        server.serve_forever()