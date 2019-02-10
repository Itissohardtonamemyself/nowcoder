# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 09:01:37 2018

@author: LX

function:一个合法的身份证号码由17位地区、日期编号和顺序编号加1位校验码组成。校验码的计算规则如下：
 首先对前17位数字加权求和，权重分配为：{7，9，10，5，8，4，2，1，6，3，7，9，10，5，8，4，2}；然后将计算的和对11取模得
 到值Z；最后按照以下关系对应Z值与校验码M的值：
 Z：0 1 2 3 4 5 6 7 8 9 10
 M：1 0 X 9 8 7 6 5 4 3 2
 现在给定一些身份证号码，请你验证校验码的有效性，并输出有问题的号码。

"""


def calculate(a):
    he = 0
    z = 0
    for i in range(0,len(a)-1):
        he = int(a[i])*quan[i] + he
    z = he%11
    return z
        
quan = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
n = input()
n = int(n)
lst = []
for i in range(0,n):
    lst.append(list(map(str,input())))
#tem = lst
#lst = tem
mo = []
for i in range(0,len(lst)):
    for j in range(0,len(lst[i])-1):
        if (lst[i][j]>='0' and lst[i][j]<='9')==False:
          mo.append(lst[i])
for i in mo:
    lst.remove(i)
zlst = [0,1,2,3,4,5,6,7,8,9,10]
mlst = ['1','0','X','9','8','7','6','5','4','3','2']
for k in lst:
    for j in range(0,len(zlst)):
        if calculate(k)==zlst[j]:
            if mlst[j]!=k[len(k)-1]:
                mo.append(k)
if len(mo)==0:
    print("All passed")
else:
    tem = ''
    out = []
    for i in mo:
        for j in i:
            tem = tem + j
        out.append(tem)
        tem = ''
    for i in out:
        print(i)
        


    