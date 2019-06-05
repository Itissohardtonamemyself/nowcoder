# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:52:54 2018

@author: LX

输入两个非负10进制整数A和B(<=230-1)，输出A+B的D (1 < D <= 10)进制数。

注意 不能写有两个while的嵌套 程序容易跑飞

"""

def count(a1,b):
    count1 = 0
    a2 = a1
    while a2>=b:
        a2 = a2//b
        count1 += 1
    a1 = a1 - b**count1
    return a1,count1


A,B,D=map(int,input().strip().split())
plus = A+B
a = plus
res = 0
cou = 1

while a>D:
    a,cou = count(a,D)
    res = res + 10**cou
if (res%10+a)>=D:
    res = res//10*10 + 10+(res%10+a)-D
else:
    res = res + a
print(res)   



#def baseN(num, b):
#    return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])
# 
#a,b,c=map(int,input().split())
#print(baseN(a+b,c))