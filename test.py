#!/bin/env python3
#-*- coding:utf8 -*-

def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >=0:
        return x
    else:
        return -x
#-----------------------------
import math

def move(x,y, step, angle=0):
    nx=x + step * math.cos(angle)
    ny=y - step * math.sin(angle)
    return nx,ny
#-------------------------------
def quad(a,b,c):
    if not isinstance(a,b,c, (int,float)):
        raise TypeError('bad operand type')
    if b**2-4*a*c <0:
        print("not result")
    else:
        x1 = (math.sqrt(b**2 - 4*a*c) - b) / (2*a)
        x2 = (-math.sqrt(b**2 - 4*a*c) - b)/ (2*a)
        return x1,x2
#-----------------------------------
#default argument
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

#print(power(3,3))

def roll(name,gender,age=20,city='BeiJing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
#roll('Tom','F',city='shanxi')

def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
#print(add_end())
#-----------------------------
#variable  argument 
def change(*number):
    sum=0
    for i in number:
        sum=sum+i*i
    return sum
