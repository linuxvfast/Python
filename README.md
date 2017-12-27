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
