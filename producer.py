import pika
credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))

channel = conn.channel() #声明一个管道

channel.queue_declare(queue='hello')  #声明一个叫hello的队列

#rabbitMQ消息不能直接发送给队列，需要经过exchange处理
channel.basic_publish(exchange='',routing_key='hello',body='hello world!')

print("[x] Sent 'Hello world!'")

conn.close()