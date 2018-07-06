import pymysql

#建立连接
conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',db='test')

#创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

r = cursor.execute('select * from test')
result = cursor.fetchone()
print(result)

#执行sql返回受影响的行数
# effect_row = cursor.execute("update test set name = 'java' where id=4 ")
# print(effect_row)
# data=[
#     ('hao',40),
#     ('jack',30),
#     ('alc',25),
# ]
#
# cursor.executemany("insert into test(name,age) values(%s,%s)",data)  #一次插入多条数据
# new_id = cursor.lastrowid   #需要在插入数据之后获取
# print(new_id)

# cursor.execute("select * from test")
# row_1 = cursor.fetchone()
# print(row_1)
# print('------')
# cursor.scroll(2,mode='absolute')
#
# row_all = cursor.fetchall()
#
# print(row_all)




conn.commit() #提交

cursor.close()#关闭游标
conn.close() #关闭连接