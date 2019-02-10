# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:04:58 2018

@author: LX

function:星际密码

"""
"""
这题目说的不清楚。。。
他意思的矩阵是长这样的：1 1
                       1 0

就是求斐波那契额数列
"""
import sys
fi = [0 for i in range(0,10001)]
fi[0],fi[1] = 1,1
for i in range(2,10001):
    fi[i] = (fi[i-1]%10000+fi[i-2]%10000)%10000
con = 0
for line in sys.stdin:
    a = line.split()
    if con%2==0:
        continue
    con+=1
    lst = list(map(int,a))
    for i in lst:
        print("%04d"%fi[i-1],end='')
    print()



