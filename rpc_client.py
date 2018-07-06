import pika
import uuid
import time,re

class FibonacciRpcClient(object):
    def __init__(self):
        self.credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            'localhost',5672,'/',self.credentials))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue  #生成随机队列

        self.channel.basic_consume(self.on_response, no_ack=True,  #on_response 回调函数
                                   queue=self.callback_queue)  #queue 对列名，从对列callback_queue接受数据

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,  #指定接受返回数据的队列
                                       correlation_id=self.corr_id,  #标记当前对列
                                   ),
                                   body=n)  #发送的内容
        while self.response is None:
            self.connection.process_data_events() #非阻塞的start_consumer
            print('no msg...')
            time.sleep(0.5)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

# print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(dir)
print(" [.] Got %r" % response)