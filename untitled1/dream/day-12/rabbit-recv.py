import pika
import time

#如果有密码就用密码认证
#credentials = pika.PlainCredentials('alex', 'alex3714')
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     host='192.168.12.112',credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='zcq',durable=True)


def callback(ch, method, properties, body):
    print(ch, method, properties)

    print(" [x] Received %r" % body)
    time.sleep(1)


channel.basic_consume(callback,
                      queue='zcq',
                      #no_ack=True       #ack知识
                      )
channel.basic_qos(prefetch_count=1)   #相当于负载均衡
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()