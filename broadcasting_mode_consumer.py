import pika

credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout'
                         )
result = channel.queue_declare(exclusive=True) #不指定queue名字,rabbit会随机分配一个名字,\
# exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue   #获取队列的名字

channel.queue_bind(exchange='logs',
                   queue=queue_name
                   )
print('waiting for logs.to exit press CTRL+C')

def callback(ch,method,properties,body):
    print('recvied from logs:%s'%body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()