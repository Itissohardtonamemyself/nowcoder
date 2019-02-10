# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:14:56 2018

@author: LX

年会抽奖

"""

#d[n] = (n-1)(d[n-1]+d[n-2])
#总：a！
d = [0,0,1]+[0 for i in range(3,21)]
f = [0,1,2]+[0 for i in range(3,21)]
for i in range(3,21):
    d[i] = (i-1)*(d[i-1]+d[i-2])
    f[i] = i*f[i-1]
try:
    while True:
        n = input()
        n = int(n)
        out = d[n]/f[n]*100
        print("%.2f"%out+"%")
except:
    pass

