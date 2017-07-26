import pika

# credentials = pika.PlainCredentials('guest','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='zcq',type='fanout')

result=channel.queue_declare(exclusive=True)  #不指定Q名，rabbit会随机分配一个名字,这里会在使用queue的消费着断开后,自动删除q

queue_name = result.method.queue #得到队列的名字


channel.queue_bind(exchange='zcq',queue=queue_name)
def callback(ch, method, properties, body):
#def callback(ch,method,properties,body):
    print('[x] %r' %body)

channel.basic_consume(callback,queue=queue_name)

channel.start_consuming()

