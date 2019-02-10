# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:13:42 2018

@author: wentong

function:D进制的A+B

"""
a,b,d = map(int,input().split())
sa = a+b
out = ''
while sa>=d:
    out = str(sa%d)+out
    sa = sa//d
out = str(sa)+out
print(out)



