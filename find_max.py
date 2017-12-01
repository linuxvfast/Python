# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:11:46 2017

@author: tony
"""

'''
#find max and max-1
s = [1,2,10,4,5,8,7]

max = s[0]
max1 = s[0]
i = 0
while i < len(s):
    if s[i] > max:
        max1 = max
        max = s[i]
    else:
        if max1 < s[i]:
            max1=s[i]    
    i += 1

print 'max1 is:',max1
print 'max is:',max
'''