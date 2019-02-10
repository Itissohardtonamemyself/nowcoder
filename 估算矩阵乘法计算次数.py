# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:37:15 2019

@author: LX

估算矩阵乘法计算次数

"""

def cal(x,y):
    res = 0
    stack = []
    for i in range(0,len(y)):
        if y[i]=='(':
            continue
        elif y[i]!=')':
            linenum = ord(y[i])-ord('A')
            stack.append(x[linenum][0])
            stack.append(x[linenum][1])
        else:
            if len(stack)!=2:
                col2 = stack.pop()
                row2 = stack.pop()
                col1 = stack.pop()
                row1 = stack.pop()
                res += row1*col1*col2
                stack.append(row1)
                stack.append(col2)
    while len(stack)!=2:
        col2 = stack.pop()
        row2 = stack.pop()
        col1 = stack.pop()
        row1 = stack.pop()
        res += row1*col1*col2
        stack.append(row1)
        stack.append(col2)
    return res


n = input()
n = int(n)
ju = []
for i in range(n):
    ju.append(list(map(int,input().split())))
s = input()
print(cal(ju,s))
