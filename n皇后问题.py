# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:38:30 2019

@author: LX

n皇后问题

"""

#n = 15
#way = (15**2)**15
#借鉴C语言代码，实现n=20

def isValid(record,i,j):
    for k in range(0,i):
        if j==record[k] or abs(record[k]-j)==abs(i-k):
            return False
    return True
def process(i,record,n):
    if i==n:#已经搜索完所有行了
        return 1
    res = 0
    for j in range(0,n):#搜索第i行每一列皇后地可能摆放位置
        if isValid(record,i,j):#如果该列可满足摆放条件，寻找下一行，并且还原现场
            record[i]=j
            res+=process(i+1,record,n)
    return res
def num1(n):
    if n<1:
        return 0
    record  = [0 for i in range(n)]
    res = process(0,record,n)
    return res
try:
    while True:
        n = input()
        if n=='':
            break
        n = int(n)
        print(num1(n))
except:
    pass