import redis

#直接连接
# r = redis.Redis(host='192.168.10.75',port=6379)
# r.set('foo','Bar')
# print(r.get('foo'))


#连接池连接
# pool = redis.ConnectionPool(host='192.168.10.75',port=6379)
#
# r = redis.Redis(connection_pool=pool)
# r.set('name','test')
# print(r.get('name'))

# source = 'Zoo'
# for i in source:
#     num = ord(i)
#     # print(num)
#     print(bin(num).replace('b',''))


import redis,time

pool = redis.ConnectionPool(host='192.168.10.75', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

pipe.set('name', 'alex')
time.sleep(50)
pipe.set('role', 'sb')

pipe.execute()