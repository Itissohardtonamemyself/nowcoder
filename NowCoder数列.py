# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 22:54:40 2018

@author: LX

NowCoder数列

"""

#f = [7%3,11%3]+[0 for i in range(2,1000001)]
#for i in range(2,1000001):
#    f[i] = (f[i-1]+f[i-2])%3  
#try:
#    while True:
#        n = input()
#        n = int(n)
#        if (n+2)%4==0:
#            print('Yes')
#        else:
#            print('No')
#except:
#    pass
lst = [0,0,1,0,0,1,0]
try:
    while True:
        n = input()
        n = int(n)
        a = (n)%8
        if lst[a]:
            print('Yes')
        else:
            print('No')
except:
    pass



