#!/usr/bin/env python3
#-*-coding:utf-8 -*-
#keep only a odd
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

#to delete an empty string
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))

#list the number back
def is_palindrome(n):
    return str(n)==str(n)[::-1] and len(str(n))>1
output=filter(is_palindrome,range(1,1000))
print(list(output))
    
