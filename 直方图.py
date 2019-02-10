# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:59:12 2018

@author: LX

直方图
"""

try:
    while True:  
        N = input()
        n = []
        for i in N:
            n.append(i)
        m = list(set(n))
        high = -1
        for i in m:
            if n.count(i)>high:
                high = n.count(i)
        lst = [[' ' for i in range(0,10)] for i in range(0,high)]+[['0','1','2','3','4','5','6','7','8','9']]
        for i in m:
            for j in range(0,10):
                if i==lst[high][j]:
                    for k in range(high-1,high-n.count(i)-1,-1):
                        lst[k][j] = '*'
        for i in range(0,high+1):
            print(''.join(lst[i]))
except:
    pass       
  
