import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
#channel = connection.channel()


# credentials = pika.PlainCredentials('zcq', '123456')
# # connection = pika.BlockingConnection(pika.ConnectionParameters(
# #     host='localhost'))
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#      host='localhost',credentials=credentials))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs',  #设置exchange名称
                         type='direct')  #类型

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'


channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()      #