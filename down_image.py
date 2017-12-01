# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:43:31 2017

@author: tony
"""

import urllib2

url=raw_input('please input a address:')
strs=urllib2.urlopen(url)

s=strs.read()
# print s

#子串的开头匹配
sub='<img'
#子串的结尾匹配
strs='.png'
#需要截取的子串长度参考
i=0
sr='http://img01.bjx.com.cn/news/UploadFile/201605/2016050310502911.png'
pop=-len(sub)
end=-len(strs)
while i<s.count(sub):
    #匹配<img开头
    pop=s.find(sub,end+len(sub)) 
    #匹配.jpg结尾
    end=s.find(strs,pop+len(strs))
    #将上面匹配到的图片地址赋值给t
    t=s[pop:end+len(strs)]
    #在字符串t中查找子串‘d6.yihaodianimg’
    http=t.find('http')
    if t[http:]==len(sr):
        url=t[http:]
        print url
    urllib.urlretrieve(url,str(i)+'.jpg')  #测试下载失败了
    #print t
    i+=1