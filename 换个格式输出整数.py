# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 11:14:12 2018

@author: LX

换个格式输出整数

"""

n = input()
n = int(n)
out = ''
for i in range(0,n//100):
    out = out+'B'
for i in range(0,n%100//10):
    out = out+'S'
for i in range(1,n%10+1):
    out = out+str(i)
print(out)
