import memcache

mc = memcache.Client(['192.168.10.75:11211'],debug=True)  #debug参数是调试使用

# mc.set('foo','99')
# mc.add('foo','wo')
# mc.replace('foo','99')

# mc.set_multi({'key1':'11','key2':'22'})
# mc.delete('foo')
# mc.delete_multi(['key1','key2'])
# ret = mc.get('foo')
# res = mc.get('key1')
# res2 = mc.get('key2')
# print(ret,res,res2)
#
# mc.append('foo','after')
# mc.prepend('foo','before')

# mc.set('k1','10')
# mc.incr('k1',10)
# mc.incr('k1')
# mc.decr('k1',9)
# print(mc.get('k1'))
# print(type(mc.get_multi(['key1','key2'])))

mc.set('product_count','899')
print(mc.get('product_count'))