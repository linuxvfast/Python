import pika
import time
credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))

channel = conn.channel()

channel.queue_declare(queue='hello')  #再次声明队列是防止消费者先启动时找不到队列报错

def callback(ch,method,properties,body):
    time.sleep(10)
    print("[x] Received %r"%body)

channel.basic_consume(callback,queue='hello') #有消费信息之后通过callbackd接收数据，声明从那个队列获取数据

print('[*] waiting for messages. to exit press CTRL+C')

channel.start_consuming()  #启动之后开始接收数据