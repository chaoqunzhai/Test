
class Alert(object):
    def send(self):
        '''报警消息发送接口'''
        raise NotImplementedError

class MailAlert(Alert):
    def send(self ):
        print('--可以调用父类的短信接口')
class SMSAlert(Alert):
    pass



m=MailAlert()       #实例化MailAlert子类
b=SMSAlert()          # 实例化SMSAlert子类
m.send()           #这里定义了send方法
b.send()      ##这里是实例 调用父类的Alert的send方法 但是你没有定义send的方法。所以会出NotImplementedError错误