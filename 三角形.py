# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:29:25 2018

@author: LX
"""

try:
    while True:
        lst = sorted(map(int,input().split()))
        if lst[2]<lst[0]+lst[1]:
            print('Yes')
        else:
            print('No')
        
except:
    pass