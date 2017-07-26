import pika
import random
import uuid
import optparse
import threading


class SSHClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-s','--server',dest='rabbit',help='rabbit server ip')
        parser.add_option('-c','--rouing key name',dest='check',help='client and server routing key')  #备注这里option 使用" " ，可解决同时存在多个-，识别错误问题
        self.options,self.args = parser.parse_args()
        self.on_connect()
        self.information = {}
        self.inforvalue = {}
        #self.task_id = random.randint(100, 800)
    def on_connect(self):
        credentials = pika.PlainCredentials('zcq', '123456')
        try:
            hosts=self.options.rabbit.split(',')
            for i in hosts:
                self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=i, credentials=credentials))
        except AttributeError as g:
            exit('*******Python3 client.py -h')
        except Exception as e:
            print('***%s not is Rabbitmq  '%i)
        self.channel = self.connection.channel()

        #self.channel.queue_declare(queue='zcq', durable=True) #声明队列
        result = self.channel.queue_declare(exclusive=True)  #声明唯一Q
        self.callback_queue = result.method.queue #Q的名字  随机生成一个Q

        #self.channel.basic_consume(self.on_response,queue=self.callback_queue)  #声明从上面那个生成的一个Q里面取消息
        #收结果并调用on_response函数

    def check_all(self,*args):
       # print('call infovalue', self.inforvalue)
        for key in self.inforvalue:
            print('[check all]----%s'%key,self.inforvalue[key])
    def on_response(self,ch,method,props,body):        #回调函数，默认就有这几个参数，props消息头
        if self.corr_id == props.correlation_id:
            self.response = body       #收到的body内容赋值给了response
          #  self.props = props
            #self.task_id = random.randint(100, 800)
            self.information[self.task_id] = props.correlation_id
            print('结果*******',body.decode('gbk'))
            del self.information[self.task_id]
            # # print('ch',ch)
            # # print('method',method)
            # print('props',props)
            # print('info...',self.information)
    def start(self):

        while True:
            self.task_id = random.randint(100, 800)
            try:
                self.sysuser = input('>>>')
            except ValueError as e:
                break
            if self.sysuser == 'q': break
            if not self.sysuser or len(self.sysuser) <2:
                continue
            struser=self.sysuser.split()[0]
            print('[用户输入str:%s] [用户输入值:%s],[TaskID:%s]' %(struser,self.sysuser,self.task_id))

            t1=threading.Thread(target=self.cmd_input,args=(struser,self.sysuser))
            t1.start()

    def call(self,struser,command):
        self.channel.basic_consume(self.on_response, queue=self.callback_queue)
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                       routing_key=self.options.check,
                                       properties = pika.BasicProperties(
                                           reply_to=self.callback_queue,         #有这么一个方法来指定Q名 这里的callback_queue就是上面声明的随机Q
                                           correlation_id=self.corr_id,         #
                                       ),
                                       body=str(command))

        print("linux command successful for Server")
      #  print('callback-queue',self.callback_queue)
        #print('corr_id',self.corr_id)
        self.inforvalue[self.task_id]= [self.callback_queue]
        # print('call info',self.information)
        # print('call infovalue',self.inforvalue)
    def check_task(self,sysuser):
     #    self.channel.basic_consume(self.on_response, queue=self.callback_queue)
     #    print('1110',self.inforvalue.get(self.task_id))
     #    print('check_task;',sysuser.split(' ')[1])
    #    print('call infovalue',self.inforvalue)
     #   print('check_task queue',self.callback_queue)
        if len(sysuser.split(' ')) == 2:
           # print('yes')

            if sysuser.split(' ')[1].isdigit():
                new=self.inforvalue.get(self.task_id)
                newqueue=str(new)
                #print('task_-',self.callback_queue)
                self.channel.basic_consume(self.on_response, queue=self.callback_queue)
                while self.response is None:  #如果没有命令返回结果
                    self.connection.process_data_events()  ##以不阻塞的形式去检测有没有新事件, 如果没有事件就什么也不做，如果有事件，就触发on_response事件，并在这个函数中给response赋
                return self.response
            else:print('init!')
        else:print('for out range')

    def cmd_input(self,struser,sysuser):
         if hasattr(self,struser):
             func=getattr(self,struser)
             func(sysuser)
         self.call(struser,sysuser)

if __name__ == '__main__':
    ssh=SSHClient()

    ssh.start()
