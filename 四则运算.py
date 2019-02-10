# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:24:53 2019

@author: LX

四则运算

"""

s = input()
s = s.replace('[','(')
s = s.replace(']',')')
s = s.replace('{','(')
s = s.replace('}',')')
print(eval(s))