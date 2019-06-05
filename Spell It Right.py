# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:57:58 2018

@author: wentong

function:Spell It Right

"""
n = input()
lst = []
for i in n:
    lst.append(int(i))
suma = 0
for i in lst:
    suma = suma + i
out = str(suma)
outlst = []
for i in out:
    if i == '0':     
        outlst.append("zero")
    if i == '1':     
        outlst.append("one")
    if i == '2':     
        outlst.append("two")
    if i == '3':     
        outlst.append("three")
    if i == '4':     
        outlst.append("four")
    if i == '5':     
        outlst.append("five")
    if i == '6':     
        outlst.append("six")
    if i == '7':     
        outlst.append("seven")
    if i == '8':     
        outlst.append("eight")
    if i == '9':     
        outlst.append("nine")
print(' '.join(outlst))
