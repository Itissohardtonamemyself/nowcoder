# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:39:05 2018

@author: wentong

function: are they equal

"""

#由于要处理的数据精度过高，用一般计算方法无法解决，所以采用字符串找标点来做
tem = list(map(str,input().split()))
n,a,b = int(tem[0]),tem[1],tem[2]
lsta,lstb = [],[]
for i in a:
    lsta.append(i)
for i in b:
    lstb.append(i)
efia,pointia,efib,pointib = -1,-1,-1,-1
for i in range(0,len(lsta)):
    if lsta[i]==".":
        pointia = i
        break
for i in range(0,len(lstb)):
    if lstb[i]==".":
        pointib = i
        break        
for i in range(0,len(lsta)):
    if lsta[i]>="1" and lsta[i]<="9":
        efia = i
        break
for i in range(0,len(lstb)):
    if lstb[i]>="1" and lstb[i]<="9":
        efib = i
        break
na,nb,temi=0,0,0
stra,strb='',''
#分类 个位数
#分类1 point没有 在0位 有效数字有、不等于0  比如12345000
if pointia==-1 and efia>=0:
    na = len(lsta)-efia
    stra = '0.'
    for i in range(0,len(lsta)):
        if lsta[i]>='1' and lsta[i]<='9':
            temi = i #取得最后标点
    if n>temi+1-efia:
        for i in range(efia,temi+1):
            stra = stra + lsta[i]
        for i in range(temi+1,n+temi):
            stra = stra + "0"
    else:
        for i in range(efia,n):
            stra = stra + lsta[i]
 
if pointib==-1 and efib>=0:
    nb = len(lstb)-efib
    strb = '0.' 
    for i in range(0,len(lstb)):
        if lstb[i]>='1' and lstb[i]<='9':
            temi = i
    if n>temi+1-efib:
        for i in range(efib,temi+1):
            strb = strb + lstb[i]
        for i in range(temi+1,n+temi):
            strb = strb + "0"
    else:
        for i in range(efib,n):
            strb = strb + lstb[i] 

#分类2 point有 有效数字没有 为0 比如0.0000
if pointia>0 and  efia==-1:
    stra = "0."
    na = 0
    for i in range(1,n+1):
        stra = stra+"0"
if pointib>0 and  efib==-1:
    strb = "0."
    nb = 0
    for i in range(1,n+1):
        strb = strb+"0"
#分类3 point有 有效数字有 且point<有效数字位 如:0.09283
if pointia>0 and efia>=0 and pointia<efia:
    na = pointia - efia + 1
    stra = '0.'
    for i in range(0,len(lsta)):
        if lsta[i]>='1' and lsta[i]<='9':
            temi = i
    if n+efia>temi:
        for i in range(efia,temi+1):
            stra = stra + lsta[i]
        for i in range(temi+1,n+efia):
            stra = stra + "0"
    else:
        for i in range(efia,n+efia):
            stra = stra + lsta[i]
if pointib>0 and efib>=0 and pointib<efib:
    nb = pointib -efib + 1
    strb = '0.'
    for i in range(0,len(lstb)):
        if lstb[i]>='1' and lstb[i]<='9':
            temi = i
    if n+efib>temi:
        for i in range(efib,temi+1):
            strb = strb + lstb[i]
        for i in range(temi+1,n+efib):
            strb = strb + "0"
    else:
        for i in range(efib,n+efib):
            strb = strb + lstb[i]
#分类4 point有 有效数字有 且point>有效数字位 如4239.897
if pointia>0 and efia>=0 and pointia>efia:
    na = pointia - efia
    stra = '0.'
    for i in range(0,len(lsta)):
        if lsta[i]>='1' and lsta[i]<='9':
            temi = i
    if n<pointia-efia:
        for i in range(efia,n+efia):
            stra = stra + lsta[i]
    elif n<temi:
        for i in range(efia,pointia):
            stra = stra + lsta[i]
        for i in range(pointia+1,n+1):
            stra = stra + lsta[i]
    else:
        for i in range(efia,pointia):
            stra = stra + lsta[i]
        for i in range(pointia+1,temi):
            stra = stra + lsta[i]
        for i in range(temi+1,n):
            stra = stra + lsta[i]
if pointib>0 and efib>=0 and pointib>efib:
    nb = pointib - efib
    strb = '0.'
    for i in range(0,len(lstb)):
        if lstb[i]>='1' and lstb[i]<='9':
            temi = i
    if n<pointib-efib:
        for i in range(efib,n+efib):
            strb = strb + lstb[i]
    elif n<temi:
        for i in range(efib,pointib):
            strb = strb + lstb[i]
        for i in range(pointib+1,n+1):
            strb = strb + lstb[i]
    else:
        for i in range(efib,pointib):
            strb = strb + lstb[i]
        for i in range(pointib+1,temi):
            strb = strb + lstb[i]
        for i in range(temi+1,n):
            strb = strb + lstb[i]
#分类5 point没有 有效数字没有
if pointia==-1 and efia==-1:
    stra = "0."
    na = 0
    for i in range(0,n):
        stra = stra + '0'
if pointib == -1 and efib==-1:
    strb = "0."
    nb = 0   
    for i in range(0,n):
        strb = strb + '0'
if stra==strb:
    outstr = stra+"*10^"+str(na)
    print("YES "+outstr)
else:
    outstra = stra+"*10^"+str(na)
    outstrb = strb+"*10^"+str(nb)
    print("NO "+outstra +" "+outstrb)

