# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:21:12 2018

@author: wentong


"""

while True:
    try:
        lst = list(map(int,raw_input().split()))
        shi,r,out = lst[0],lst[1],''
        while shi>=r:    
            if shi%r<10:
                out = str(shi%r) + out
            elif shi%r==10:
                out = 'A'+out
            elif shi%r==11:
                out = 'B'+out
            elif shi%r==12:
                out = 'C'+out
            elif shi%r==13:
                out = 'D'+out
            elif shi%r==14:
                out = 'E'+out
            elif shi%r==15:
                out='F'+out
            shi = shi//r
        if shi<10:
            out = str(shi) + out
        elif shi==10:
            out = 'A'+out
        elif shi==11:
            out = 'B'+out
        elif shi==12:
            out = 'C'+out
        elif shi==13:
            out = 'D'+out
        elif shi==14:
            out = 'E'+out
        elif shi==15:
            out='F'+out
        print out
    except:
        break