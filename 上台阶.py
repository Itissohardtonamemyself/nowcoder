# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:35:07 2019

@author: LX

上台阶

"""

#1-0 2-1 3-2 4-3
#res[n]相当于分为：少跨一个台阶和少跨两个台阶的方法之和
class GoUpstairs:
    def countWays(self, n):
        # write code here
        mod = 1000000007
        res = [0 for i in range(n)]
        res[0],res[1],res[2] = 0,1,2
        for i in range(3,n):
            res[i] = res[i-1]+res[i-2]
            res[i] = res[i]%mod
        return res[n-1]