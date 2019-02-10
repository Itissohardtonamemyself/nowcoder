# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:36:22 2019

@author: LX

斐波那契数列加强版
(递归，动态规划，高级结构)
#这个矩阵快速幂可以把问题拆分为矩阵乘法和快速幂乘法两部分完成。


"""

class Fibonacci:
    def getNthNumber(self,n):
        mod = 1000000007
        res = [[1,1],[1,0]]#结果项
        surplus = [[1,0],[0,1]]#surplus存储剩余项
        while n>1:
            if n&1:
                surplus = self.mutiply(surplus,res)
            res = self.mutiply(res,res)
            n = n>>1   #按照位运算，更加快速解决问题。
        res = self.mutiply(res,surplus)
        return res[0][0]%mod
   
    def mutiply(self,a,b):#矩阵乘法
        mod = 1000000007
        temp = [[0,0],[0,0]]
        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(temp)):
                    temp[i][j]+=a[i][k]*b[k][j]%mod
        return temp