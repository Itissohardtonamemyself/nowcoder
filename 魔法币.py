# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:01:55 2018

@author: LX

魔法币

"""

def mac1(a):
    return (a-1)//2
def mac2(a):
    return (a-2)//2

n = input()
n = int(n)
out = ''
while n>0:
    if n%2==0:
        n = mac2(n)
        out = '2'+out
    else:
        n = mac1(n)
        out = '1'+out
print(out)
    