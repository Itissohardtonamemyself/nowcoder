# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:10:23 2018

@author: LX

通过键盘输入一串小写字母(a~z)组成的字符串。
请编写一个字符串归一化程序，统计字符串中相同字符出现的次数，并按字典序输出字符及其出现次数。
例如字符串"babcc"归一化后为"a1b2c2"

"""

n = input().strip().split()
lst = []
for i in n[0]:
    lst.append(i)
coulst = [0 for i in range(0,26)]
zimu = 'abcdefghijklmnopqrstuvwxyz'
zimulst = []
for j in zimu:
    zimulst.append(j)
for i in range(0,len(lst)):
    for j in range(0,len(zimulst)):
        if lst[i] == zimulst[j]:
           coulst[j] += 1

indexlst = []
for i in range(0,len(coulst)):
    if coulst[i]!=0:
        indexlst.append(i)
string = ''
for i in range(0,len(indexlst)):
    string = string + zimulst[indexlst[i]]+str(coulst[indexlst[i]])
print(string)