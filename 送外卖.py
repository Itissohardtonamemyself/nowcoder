# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 09:57:32 2018

@author: LX

送外卖

"""
try:
    while True:
        m, n = list(map(int, input().split()))
        if m%2 == 0 or n%2 == 0:
            print(str(m*n)+'.00')
        else:
            print(str(m*n)+'.41')
except:
    pass
    


