# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:14:56 2017

@author: tony
"""


s='ab123456dfadf'
strs='abdf'
i=q=e=0

while i<len(s):
    if s[i] not in strs:
        q=i
        break
    i+=1
s=s[q:]
print s

i=len(s)-1
while i>=0:
    #print s[i],
    if s[i] not in strs:
        e=i+1
        break
    i-=1
print s[:e]
