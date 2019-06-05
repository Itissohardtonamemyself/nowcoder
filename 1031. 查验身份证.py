# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:35:36 2018

@author: LX

1031. 查验身份证

"""
quan = ['7','9','10','5','8','4','2','1','6','3','7','9','10','5','8','4','2']
z = ['0','1','2','3','4','5','6','7','8','9','10']
m = ['1','0','X','9','8','7','6','5','4','3','2']
n = input()
n = int(n)
boo = True
for i in range(0,n):
    temlst,he,boo1 = [],0,True
    tem = input()
    for i in tem:
        temlst.append(i)
    for i in temlst:
        if (i>="0" and i<='9')==False:
            boo = False
            boo1 = False
            print(tem)
            break
    if boo1:
        for i in range(0,17):
            he+=int(temlst[i])*int(quan[i])
        if m[z.index(str(he%11))]!=temlst[-1]:
            print(tem)
            boo = False
if boo:
    print("All passed")
    
