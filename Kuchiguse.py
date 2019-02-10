# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:44:19 2018

@author: LX

Kuchiguse

"""

n = input()
n = int(n)
lst = []
for i in range(n):
    word = input()
    te = []
    for i in word:
        te.append(i)
    te.reverse()
    lst.append(te)
lst.sort(key=lambda x:(len(x)))
out = []
boo = True
for q in range(0,len(lst[0])):
    for i in lst:
        if lst[0][q]!=i[q]:
            boo = False
            break
    if boo:
         out.append(lst[0][q])
    else:
        break
out.reverse()
if out:
    outstr = ''
    for i in out:
        outstr+=i
    print(outstr)
else:
    print("nai")
    
    
