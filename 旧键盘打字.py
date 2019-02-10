# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:47:19 2018

@author: LX

旧键盘打字

"""
boo = False
pkey = '+'
s1 = input()
s2 = input()
for i in pkey:
    if i in s1:
        boo = True
        s1 = s1.replace(i,'')
if boo:
    for i in s2:
        if i>='A' and i<='Z':
            s2 = s2.replace(i,'')
for i in s2:
    if (i.upper() in s1) or  (i.lower() in s1):
        s2 = s2.replace(i,'')
if s2:
    print(s2)
else:
    print()