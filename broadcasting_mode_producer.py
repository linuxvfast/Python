import pika,sys

credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'info:Hello world!'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print('send data:',message)
connection.close()