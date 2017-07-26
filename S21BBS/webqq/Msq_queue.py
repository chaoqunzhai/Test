import time
import queue

class MsgHandler(object):
    def __init__(self,request,msg_queue):
        self.request = request
        self.msg_queue = msg_queue

        '''因为在前端dashboard页面中，已经定制了一个data的数据，并通过post的方式传输到后台，
        所以这里在生成一个特定的格式  '''
    def get_msg_data(self):
        data={}
        data['from']=self.request.POST.get("from")
        data['to']=self.request.POST.get("to")
        data['data']=self.request.POST.get("data")
        data['date'] = time.time()
        '''返回一个干净的data数据'''
        return data
    def msg_send(self):
        msg_data = self.get_msg_data()
        print("msg_data",msg_data)
        if msg_data["to"] not in self.msg_queue:
            self.msg_queue[msg_data['to']] = queue.Queue()

        self.msg_queue[msg_data['to']].put(msg_data)

    def msg_recv(self):
        '''这里的request.user.userprofile.id 其实已经在前端中定义了'''
        user = self.request.user.userproifle
        print('user——id',self.request.user.userproifle.id)
        print("一共多少个队列",self.msg_queue)
        ''''''
        if str(user.id) in self.msg_queue:
            print("去Queue中取消息",user.id,user.name)
            '''get 如果没有数据就会挂起'''
            msg_data = self.msg_queue[str(user.id)].get(timeout=3)
            print('recv_msg_data',msg_data)
            return msg_data
        else:

            '''如果没有数据，也返回一个字段，这样前端好处理'''
            print("没有数据----！！！")
            self.msg_queue[str(user.id)] = queue.Queue()
            msg_data = self.msg_queue[str(user.id)].get()

            return msg_data