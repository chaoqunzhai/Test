import pika
#创建一个类似于socket连接
credentials = pika.PlainCredentials('zcq', '123456')
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=url_1,
#                                      credentials=credentials, ssl=ssl, port=port))
connection = pika.BlockingConnection(pika.ConnectionParameters(
     host='192.168.1.10',credentials=credentials))
# connection = pika.BlockingConnection(pika.ConnectionParameters(
#     host='localhost'))
channel = connection.channel()       #商议好协议

# 声明queue
channel.queue_declare(queue='zcq',durable=True)          #声明Q   durable为设置为持久化   Q名必须唯一

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='zcq', #send msg to this queue  发送到哪个Q里面
                      body='zhaichaoqun',           #消息内容
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent         持久化  如果Q设置为持久化  消息也必须设置持久化
                      )
                      )
print(" [x] Sent 'Hello World!2'")
connection.close()