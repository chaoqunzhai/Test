import pika
import sys

#生产者
#
#如果需要密码 这里指定密码
#credentials = pika.PlainCredentials('guest','guest')
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'，credentials=credentials ))
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()  #channel 绑定的意思,即routing key，就好比，每个邮局把信件送到你家邮箱的一条路线

channel.exchange_declare(exchange='zcq',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or 'hellow-----'

channel.basic_publish(exchange='zcq',
                      routing_key='',
                      body=message)

print('--%s--'%message)
connection.close()

