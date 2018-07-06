import pika
credentilals = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost',5672,'/',credentilals))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()