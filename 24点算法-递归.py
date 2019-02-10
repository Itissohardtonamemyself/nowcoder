# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:38:18 2019

@author: LX

24点算法-递归

"""

def swap(a,b):
    a,b = b,a
    return a,b
def is24(a,begin,end,tot):
    if begin==end-1:
        return a[begin]==tot
    else:
        ans = False
        for i in range(begin,end):
            a[i],a[end-1] = swap(a[i],a[end-1])
            ans = ans or is24(a,begin,end-1,tot+a[end-1]) or is24(a,begin,end-1,tot-a[end-1]) or is24(a,begin,end-1,tot*a[end-1]) or is24(a,begin,end-1,tot/a[end-1])
            a[i],a[end-1] = swap(a[i],a[end-1])
        return ans
try:
    while True:
            a = list(map(int,input().split()))
            if is24(a,0,4,24):
                print('true')
            else:
                print('false')
except:
    pass