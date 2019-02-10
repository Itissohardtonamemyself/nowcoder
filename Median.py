# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:33:21 2018

@author: wentong

function:1029. Median

"""

a = list(map(int,input().split()))
b = list(map(int,input().split()))
lst = a[1:]+b[1:]
lst.sort()
if len(lst)%2!=0:
    print(lst[len(lst)//2])
else:
    print(lst[len(lst)//2-1])