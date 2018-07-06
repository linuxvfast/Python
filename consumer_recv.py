import pika, time
credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue',durable=True)
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print('--->',ch,method.delivery_tag)
    # time.sleep(30)
    print(" [x] Done")
    # print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag = method.delivery_tag)  #客户端循环接收

channel.basic_qos(prefetch_count=1)  #实现公平分发任务，处理快的多分发
channel.basic_consume(callback,
                      queue='task_queue',
                      # no_ack=True    #不确认客户端是否收到消息，如果加不确认参数，rabbitmq默认是有消息确认的，\
                      #当客户端掉线之后，重启新的客户端之后会重新接收生产者发送的数据
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()