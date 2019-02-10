# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:07:27 2018

@author: LX
"""

fi = [0 for i in range(0,10001)]
fi[0],fi[1] = 1,1
for i in range(2,10001):
    fi[i] = (fi[i-1]+fi[i-2])%10000
    
while True:
    try:
        n = input()
        lst = list(map(int,raw_input().split()))
        ans= []
        for i in lst:
            ans.append("%04d"%fi[i-1])
        print ''.join(ans)
    except:
        break