import memcache

mm = memcache.Client(['192.168.10.75:11211'],debug=True,cache_cas=True)
# mm.set('product_count','899')
# print(mm.get('product_count'))

v = mm.gets('product_count')
print(v)
mm.set('product_count','899')
mm.cas('product_count','855')