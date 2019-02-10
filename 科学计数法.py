# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:10:25 2018

@author: LX
"""
N = input()
lst = []
num = ''
zhi = []
zhu = ''
zhiindex = 0
for i in N:
    if i == 'E':
        break
    else:
        num = num + i
for i in N:
    lst.append(i)
for j in range(0,len(lst)):
    if lst[j] == 'E':
        zhiindex = j+1
        break
zhi = lst[zhiindex:len(lst)]
for k in range(0,len(zhi)):
    zhu = zhu + zhi[k]
num1 = []
number = 0.0
numzf = 0
zhu1 = []
zhuber = 0
zhuzf = 0
for i in num:
    if i=='-':
        numzf = -1
    elif i!='+' and i!='-' and i!='.':
        num1.append(int(i))
    elif i=='+':
        numzf = 1
for i in range(0,len(num1)):
    number = (num1[i])*(10**(-i))+number
number = round(number,len(num1))

for j in zhu:
    if j=='-':
        zhuzf = -1
    elif j!='+' and j!='-':
        zhu1.append(int(j))
    elif j=='+':
        zhuzf = 1
temp = 0
for j in range(0,len(zhu1)):
    if zhu1[j] != 0:
        temp=j
        break
for k in range(temp,len(zhu1)):
    zhuber = zhuber + zhu1[len(zhu1)-k-1]*(10**(k-temp))

jingque = 0
res = 0
jingquestr = ''
if zhuzf==-1:
    jingque = zhuber+len(num1)-1
    res = (10**(-zhuber))*number*numzf
    jingquestr = "%."+str(jingque)+"f"
    print(jingquestr%(res))
elif zhuzf==1:
    if len(num1)-zhuber-1>0:
        jingque = len(num1)-1- zhuber
        res = (10**(zhuber))*number*numzf
        jingquestr = "%."+str(jingque)+"f"
        print(jingquestr%(res))
    else:
        temper = len(num1)-1
        res = int(number*(10**temper))*numzf*(10**(zhuber-temper))
        res = str(res)
        print(res)
else:
    jingque = len(num1)-1
    jingquestr = "%."+str(jingque)+"f"
    print(jingquestr%(number))

#from __future__ import print_function
# 
#sci = input()
#ixE = sci.find('E')
# 
#if '-'==sci[0]:
#    print('-', end='')
# 
#part1 = sci[1]
#part2 = sci[3:ixE]
#len2 = len(part2)
#e = int(sci[ixE+1:])
# 
#if e>0:
#    if e<len2:
#        print( part1+part2[:e]+'.'+part2[e:len2] )
#    else:
#        print( part1+part2+(e-len2)*'0' )
#elif e==0:
#    print(sci[1:ixE])#左包含 右边不包含
#else:
#    e = -e
#    print( '0.'+'0'*(e-1)+part1+part2 )

