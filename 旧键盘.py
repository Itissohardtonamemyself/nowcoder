# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 23:19:25 2018

@author: LX

function:旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。现在给出应该输入的一段文字、以及实际被输入的文字，请你列出
肯定坏掉的那些键。

注意：remove()方法和del 命令不同的地方：
remove()只能移除第一个出现的具体的东西，而del可以做到移除指定位置的内容
    
"""
si = list(input())
so = list(input())
sia = list(set(si))
soa = list(set(so))
for i in soa:
    sia.remove(i)
temp = []
index = []
for i in range(0,len(sia)):
    for j in range(0,len(si)):
        if sia[i]==si[j]:
            temp.append(j)
    index.append(temp)
    temp = []
for i in range(0,len(index)):
    index[i] = min(index[i])
index.sort()
String = []
for i in index:
    String.append(si[i])
exam = 'abcdefghijklmnopqrstuvwxyz'
for k in range(0,len(String)):
    if String[k] in exam:
        String[k] = String[k].upper()
res = []
for i in range(0,len(String)):
    for j in range(i+1,len(String)):
        if String[i]==String[j]:
            res.append(j)
res.sort()
while len(res)>0:
    del String[res[0]]
    res.remove(res[0])
    for i in range(0,len(res)):
        res[i]=res[i]-1    
out=''
for i in String:
    out = out + i
print(out)

