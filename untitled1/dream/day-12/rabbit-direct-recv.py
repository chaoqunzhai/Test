import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='direct_logs',   #指定exchange名称
                         type='direct')

result = channel.queue_declare(exclusive=True)  ##不指定Q名，rabbit会随机分配一个名字,这里会在使用queue的消费着断开后,自动删除q
queue_name = result.method.queue  #得到Q名称  recv端必须指定queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:  #循环 severities 列表 得到用户输入值   然后传入到routing_key 来绑定
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)          #exchange 接收到消息。然后把消息交给Q里，这里是指定Q，如果不指定，就丢失了消息

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming() #开始接受