# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:43:03 2018

@author: LX

function: color in mars

"""
def tran(a):
    shi = a//13
    ge = a%13
    if shi<10:
        out1 = str(shi)
    elif shi==10:
        out1 = "A"
    elif shi==11:
        out1 = "B"
    elif shi==12:
        out1 = "C"
    if ge<10:
        out2 = str(ge)
    elif ge==10:
        out2 = "A"
    elif ge==11:
        out2 = "B"
    elif ge==12:
        out2 = "C"
    return out1+out2
lst = list(map(int,input().split()))
print("#"+tran(lst[0])+tran(lst[1])+tran(lst[2]))
