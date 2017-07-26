import pika
import subprocess
import optparse

class SSHServer(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option('-c', '--rouing key name', dest='check', help='client and server routing key')
        self.options, self.args = parser.parse_args()
        self.on_connect()

    def on_connect(self):
        credentials = pika.PlainCredentials('zcq', '123456')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='127.0.0.1', credentials=credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.options.check)


    def command(self,cmd):
       # print(cmd)
        cmd_obj = subprocess.Popen(cmd.decode(),shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        result = cmd_obj.stdout.read() #chuli
        print(cmd_obj.stderr.read())
        return result
    def on_request(self,ch,method,props,body):
        print('client command',body)
        response = self.command(body)

        ch.basic_publish(exchange='',
                         routing_key = props.reply_to,
                         properties=pika.BasicProperties(correlation_id=
                                                         props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print('pro',props)
        print('ch',ch)
        print('method',method)
        print('body',body)
    def start(self):
        self.channel.basic_consume(self.on_request,queue=self.options.check)

        self.channel.start_consuming()
if __name__ == '__main__':
    a=SSHServer()
    a.start()