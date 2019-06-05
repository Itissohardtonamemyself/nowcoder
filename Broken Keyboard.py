# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:00:01 2018

@author: LX

Broken Keyboard

"""
n = input()
m = input()
tem = set([])
for i in n:
    if i not in m:
        tem.add(i.upper())
out = ''
for i in n:
    if i.upper() in tem:
        out+=i.upper()
        tem.remove(i.upper())
        if len(tem)==0:
            break
print(out)