# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:49:45 2019

@author: LX

上楼梯

"""

# -*- coding:utf-8 -*-
#1-1,2-2,3-3,4-5,5-8,6-13 f(n) = f(n-1) + f(n-2)
#1-1,2-2,3-4-0*2+1,4-7-1*2,5-13-2*2+1,6-24-5*2+1,7--5*2+1+5
#f(n) = f(n-1)+f(n-2)+f(n-3)
mod = 1000000007
ran = 100000
f = [0 for i in range(ran)]
f[0],f[1],f[2],f[3] = 0,1,2,4
for i in range(4,ran):
    f[i] = (f[i-1]+f[i-2]+f[i-3])%mod

class GoUpstairs:
    def countWays(self, n):
        # write code here
        return f[n]
        