import pika
import time,os

credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost',5672,'/',credentials))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    data = os.system(n)
    print(data)
    return data
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):

    response = fib(body)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to, #获取客户端指定的接收消息队列
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id), #获取客户端提供的队列标记id
                     body=response)  #发送fib函数处理后的结果
    ch.basic_ack(delivery_tag=method.delivery_tag) #发送消息确认



channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()