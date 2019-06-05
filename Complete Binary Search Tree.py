# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:06:59 2018

@author: LX

Complete Binary Search Tree

"""


def ran(root):
    if root>=n:
        return
    ran(root*2+1)
    out[root] = lst.pop()
    ran(root*2+2)
n = input()
n = int(n)
out = [None]*n
lst = sorted(map(int,input().split()))
lst.reverse()
ran(0)
print(" ".join(map(str,out)))
