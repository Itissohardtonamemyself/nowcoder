# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:55:29 2018

@author: wentong

母牛的故事

"""

#1 2 3 4 6 9 13
#当n>4时，n[i] = n[i-1]+n[i-3]
lst = [1,2,3,4]+[0 for i in range(4,55)]
for i in range(4,55):
    lst[i] = lst[i-1]+lst[i-3]
try:
    while True:
        n = input()
        n = int(n)
        print(lst[n-1])
except:
    pass
