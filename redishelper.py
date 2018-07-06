import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.10.75')   #直接连接redis服务器
        self.chan_sub = 'fm104.5'  #定义频道
        self.chan_pub = 'fm104.5'

    def public(self, msg):   #发布
        self.__conn.publish(self.chan_pub, msg)   #发布消息，指定频道和消息
        return True

    def subscribe(self):  #订阅
        pub = self.__conn.pubsub()   #订阅消息
        pub.subscribe(self.chan_sub)  #订阅管道
        pub.parse_response()   #准备接收数据
        return pub