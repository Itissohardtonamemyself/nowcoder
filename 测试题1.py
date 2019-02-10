# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:57:37 2018

@author: LX

测试题1

"""


lst = []
for i in range(1,63):
    lst.append(2**i)
lst1 = []
for i in range(62):
    for j in range(i+1,62):
        lst1.append(lst[i]+lst[j])
lst.remove(2)
t = input()
t = int(t)
for i in range(t):
    num = input()
    num = int(num)
    if num in list(lst1)+lst:
        print("YES")
    else:
        print("NO")
