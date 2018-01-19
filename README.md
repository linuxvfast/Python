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

assertEqual(a, b)        核实a == b

assertNotEqual(a, b)     核实a != b

assertTrue(x)            核实x 为True

assertFalse(x)           核实x 为False

assertIn(item , list )   核实  item 在  list 中

assertNotIn(item , list ) 核实  item 不在  list 中


断言测试例子
names.py
#-*- coding:utf-8 -*-
#function 1
# import unittest
# from name_function import get_formatted_name
#
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name:")
#     if first == 'q':
#         break
#     middle = input("Please give me a middle name:")
#     if middle == 'q':
#         break
#     last = input("Please give me a last name:")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first,middle,last)
#     print("\tNeatly formatted name: " + formatted_name + ".")

#print("==========================================")
#function 2
import unittest
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break
    population = input("Please give me a population name:")
    if population == 'q':
        break
    formatted_name = get_formatted_name(first,last,population)
    print("\tNeatly formatted name: " + formatted_name + ".")
  ------------------------------------------------------------  
    
name_function.py
#-*- coding:utf-8-*-
#function 1
# def get_formatted_name(first,last,middle=''):
#     '''Generate a neatly formatted full name.'''
#     if middle:
#         full_name = first + ' ' + middle + ' ' + last
#     else:
#         full_name = first + ' ' + last
#     return full_name.title()

#print("============================================")
#function 2
def get_formatted_name(first,last,population=''):
    '''Generate a neatly formatted full name.'''
    if population:
        full_name = first + ',' + last + ' - ' + 'population ' + str(population)
        return full_name.split("-")[0].title() + '-' + full_name.split("-")[1]
    else:
        full_name = first + ',' + last
        return full_name.title()
     --------------------------------------------------------------------   
  test_name_function.py
  #-*- coding:utf-8-*-
#function 1
# import unittest
# from name_function import get_formatted_name
#
# class NameTestCase(unittest.TestCase):
#     '''测试name_function.py'''
#     def test_first_last_name(self):
#         '''能正确的处理像tian jun这样的姓名?'''
#         formatted_name = get_formatted_name('janis','jopin')
#         self.assertEqual(formatted_name,'Janis Jopin')
#
#     def test_first_last_middle_name(self):
#         '''能够正确地处理xi yang yang 这样的姓名吗?'''
#         formatted_name = get_formatted_name('xi','yang','yang')
#         self.assertEqual(formatted_name,'Xi Yang Yang')
#
# unittest.main()


import unittest
from name_function import get_formatted_name
class CityNameTset(unittest.TestCase):
    '''test name_function.py'''
    def test_city_country(self):
        '''能正确的处理像tian jun这样的国家和城市的结合名称?'''
        formated_name = get_formatted_name('china','tang shan')
        self.assertEqual(formated_name,'China,Tang Shan')
    def test_city_country_population(self):
        '''能正确的处理像China,TangShan - population xxxx这样的结合名称?'''
        formated_name = get_formatted_name('china','tang shan',50000)
        self.assertEqual(formated_name,'China,Tang Shan - population 50000')

unittest.main()
=============================================================
setUp()简化测试

变量名前加self，表示将数据存储在属性中，如下例子

# -*- coding:utf-8 -*-
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类进行测试'''

    def setUp(self):
        '''创建一个调查对象和一组答案，供测试方法使用'''
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Chinese','Spanish']


    def test_store_single_response(self):
        '''测试存储单个答案'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        '''测试存储三个答案'''
        for x in self.responses:
            self.my_survey.store_response(x)

        for x in self.responses:
            self.assertIn(x,self.my_survey.responses)

unittest.main()
=================================================================
运行测试脚本时，完成一个单元测试，python打印一个字符，测试通过时打印一个句点，测试报错时打印一个E，测试导致断言失败打印F

····································································
绘制图形
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]    #图形点
input_value = [1,2,3,4,5]   #x轴坐标值
plt.plot(input_value,squares,linewidth=5)  #linewidth 表示线条的粗细

#设置图标的标题，给坐标添加标签
plt.title("Square Numbers",fontsize=24)    #fontsize表示字体的大小
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
# plt.tick_params('x',labelsize=5)   #labelsize表示坐标轴的字体大小
plt.tick_params(labelsize=15)   #默认是坐标轴的字体都设置
plt.show()
