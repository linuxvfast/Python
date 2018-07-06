import pika,sys

credentials = pika.PlainCredentials('rabbitmqtest','rabbit!@#test123')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='ram',exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'waiting'   #过滤条件
message = ' '.join(sys.argv[2:]) or 'info:Hello world!'
channel.basic_publish(exchange='ram',
                      routing_key=severity,
                      body=message)

print('send data:',message)
connection.close()