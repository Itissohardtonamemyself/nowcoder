# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:45:18 2018

@author: wentong

function:数位和

"""

def tran(num,n):
    global s
    out=''
    while num:
        out = s[num%n] + out
        num = num//n
    return out
while True:
    try:
        s='0123456789ABCDEFG'
        lst = list(map(int,raw_input().split()))
        num,r,out = lst[0],lst[1],''
        tem = tran(num,r)
        he = 0 
        for i in tem:
            he+= s.find(i)
        out  = tran(he,r)
        print out
        
    except:
        break