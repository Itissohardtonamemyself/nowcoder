# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:46:04 2019

@author: LX

超长正整数相加

"""

try:
    while True:
        s1 = input()
        s2 = input()
        if len(s1)>len(s2):
            s2 = (len(s1)-len(s2))*'0'+s2
        elif len(s1)<len(s2):
            s1 = (len(s2)-len(s1))*'0'+s1
        l = len(s1)
        out = ''
        temp = 0
        for i in range(l-1,-1,-1):
            t = int(s1[i])+int(s2[i])+temp
            if t>=10:
                temp = 1
                t = t-10
            else:
                temp = 0
            out = str(t)+out
        if temp==1:
            out = '1'+out
        print(out)
except:
    pass