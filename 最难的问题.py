# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 09:54:24 2018

@author: LX

最难的问题

"""

stmi = ['A','B','C','D','E', 'F' ,'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
styuan = ['V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U']

try:
    while True:
        n= input()
        if n=='':
            break
        out = []
        for i in n:
            if i in styuan:
                out.append(styuan[stmi.index(i)])
            else:
                out.append(i)
        print(''.join(out))   
except:
    pass

