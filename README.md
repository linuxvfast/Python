list的insert
把一个列表插入到另一个列表中指定的位置，按从小到大的顺序
s1插入到 s2中指定的位置
i=0,循环插入
在insert中指定位置插入的值应该为s1[len(s1)-1-i]


extend
可以直接省略遍历追加到其他的列表中

append添加列表到其他的列表中时，需要遍历之后append追加到遍历中

set函数可以去重，是一个无序的元素集合

list.index(value,[start,[stop]])
返回值value所在列表的索引值



自定义模块，需要在*.pth文件中指定自定义模块的存放路径，一般存放在C:\Python27\site-packages下，也可以自定义路径

例子
fa = open(r'D:\python\a.txt','r')  #打开文件
cout = fa.readline()  #读取一行数据
#去除行中的换行符
print cout.strip("\n")
#关闭文件
fa.close()


mysql》》select * from tb2 where exists(select * from tb1 where id < 5);

#如果exists的结果为真，前面的select语句可以得到结果，如果exists的结果为假，前面的select没有查询结果


where条件后接  any（sql语句）或者all（sql语句） 可以多表查询

#union 将两个等长字段的表连接显示
mysql> select * from tb1 union select *  from tb3;
+------+------+------+
| id   | name | year |
+------+------+------+
| 4    | tom  | 1995 |
| 1    | ask  | 1999 |
| 4    | key  | 1995 |
| 5    | jon  | 1991 |
| 3    | a    | 1992 |
| tom  | f    |    2 |
+------+------+------+
6 rows in set (0.00 sec)



# left  join 和right join的使用
mysql> select b2.*,b1.* from b2 left join b1 on b1.size = b2.size;   #以b2为基准，用b1的匹配，看b2中有b1的什么
+------+------+------+------+
| size | name | id   | size |
+------+------+------+------+
|   10 | ask  |    1 |   10 |
|   20 | key  |    2 |   20 |
|   30 | aaa  |    3 |   30 |
|   40 | bbba | NULL | NULL |
|   50 | cccc | NULL | NULL |
+------+------+------+------+
5 rows in set (0.02 sec)

mysql> select * from b2 left join b1 on (b1.size = b2.size )where name='key';
+------+------+------+------+
| size | name | id   | size |
+------+------+------+------+
|   20 | key  |    2 |   20 |
+------+------+------+------+
1 row in set (0.00 sec)

mysql> select * from b1 left join b2 on b1.size = b2.size;
+------+------+------+------+
| id   | size | size | name |
+------+------+------+------+
|    1 |   10 |   10 | ask  |
|    2 |   20 |   20 | key  |
|    3 |   30 |   30 | aaa  |
+------+------+------+------+
3 rows in set (0.00 sec)

mysql> select * from b1 right join b2 on b1.size = b2.size;   #以b2位基准，匹配b1中有的
+------+------+------+------+
| id   | size | size | name |
+------+------+------+------+
|    1 |   10 |   10 | ask  |
|    2 |   20 |   20 | key  |
|    3 |   30 |   30 | aaa  |
| NULL | NULL |   40 | bbba |
| NULL | NULL |   50 | cccc |
+------+------+------+------+
5 rows in set (0.00 sec)

mysql> select * from b2 right join b1 on b1.size = b2.size;
+------+------+------+------+
| size | name | id   | size |
+------+------+------+------+
|   10 | ask  |    1 |   10 |
|   20 | key  |    2 |   20 |
|   30 | aaa  |    3 |   30 |
+------+------+------+------+
3 rows in set (0.00 sec)



================================
import psutil

#mem = psutil.virtual_memory()   #获取内存的完整信息
psutil.swap_memory()  #获取交换内存的信息
#print mem.total,mem.used
print psutil.cpu_times()  #显示所有的cpu信息
print psutil.cpu_times(percpu=True)   #显示所有的逻辑cpu信息
print psutil.cpu_times().user  #显示单个数据
print psutil.cpu_count()   #显示服务器的cpu逻辑个数
print psutil.cpu_count(logical=False) #显示服务器的物理cpu个数

print psutil.disk_partitions()   #获取磁盘信息
print psutil.disk_usage('/')   #获取磁盘的分区使用情况
ss = psutil.disk_io_counters(perdisk=True)    #不加参数perdisk获取磁盘总的io个数和读写信息，加参数获取单个磁盘的io个数和读写信息

for k,v in ss.items():
    print k,v
    
print  psutil.net_io_counters()  #获取网络总的io信息，可以加参数(pernic=True)获取单个网络接口的io信息
====================================================================
数据存储 
json.dump() #将数据转储到文件
json.load()  #从文件中读取数据

例子：
#-*- coding:utf-8 -*-

import json
# numbers = [2.3,4,7,11,13]

filename = 'test.json'
# with open(filename,'w') as file_obj:
#     json.dump(numbers,file_obj)

with open(filename) as file_read:
    lins = json.load(file_read)
    print(lins)
=========================================================
unittest modle中的断言方法
assertEqual(a, b)      的  核实a == b
assertNotEqual(a, b)     核实a != b
assertTrue(x)            核实x 为True
assertFalse(x)           核实x 为False
assertIn(item , list )   核实  item 在  list 中
assertNotIn(item , list ) 核实  item 不在  list 中
