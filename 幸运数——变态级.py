# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:09:04 2018

@author: wentong

LUCKY STRING

A string s is LUCKY if and only if the number of different characters in s is a fibonacci number. Given a string consisting of only lower case letters , output all its lucky non-empty substrings in lexicographical order. 
Same substrings should be printed once. 

    
    res = []
    for k in range(0,len(lSmoi)):
        for k1 in range(0,len(lfoaq)):
            if lSmoi[k] == lfoaq[k1]:
                res.append(lSmoi[k])
    for i in range(0,len(lSr)):
        for j in range(0,len(lSmo)):
            if lSr[i] == lSmo[j]:
                lSmoi += 1
"""
#造一个斐波那契数列 由于输入字符小于100 斐波那契数小于101
#def remo(a,index):
#    for i in range(0,len(a)):
#        if i>=len(a):
#                break
#        else:
#            if index[i]!=0:
#                a = a[:i]+a[i+1:]
#                index = index[:i]+index[i+1:]     
#    return a
#    
def paixu(x):
    for i in range(0,len(x)-1):
        for j in range(0,len(x)-1-i):
            if x[j]>x[j+1]:
                x[j],x[j+1] = x[j+1],x[j] 
    return x
def diff(String1):
    lsubstr = []
    substr = ''
    for i in range(1,len(String1)+1):
        for j in range(0,i):
            substr = substr+String1[j]
        lsubstr.append(substr)
        substr = ''
    return lsubstr
#def select(sr):
#    smo = 'abcdefghijklmnopqrstuvwxyz'
#    lSmo = []
#    lSri= []
#    lSr = []
#    length =0
#    for i in smo:
#        lSmo.append(i)       
#    for j in sr:
#        lSr.append(j)
#        lSri.append(0)
#    #除掉不同的字符
#    for i in range(0,len(lSr)):
#        for j in range(i+1,len(lSr)):
#            if lSr[i] == lSr[j] and lSr[i]!=0:
#                lSr[j] = 0 
#                lSri[j]= 1
##    for i in range(0,len(lSri)):
##        if lSri[i] == 0:
##            lSr.remove(lSr[i])
#    length = len(lSr)-sum(lSri)
#    for k in range(0,len(lfoaq)):
#        if length == lfoaq[k]:
#            return sr
#    return 0
def isLucky(a):
    if len(set(a)) in lfoaq:
        return True
    else:
        return False


lfoaq = []
a1 = 1
a2 = 1
lfoaq.append(a1)
lfoaq.append(a2)
for i in range(1,101):
    a1 = a1 + a2
    if a1>26:
        break
    lfoaq.append(a1)
    a2 = a1 + a2
    if a2>26:
        break
    lfoaq.append(a2)
    
s = input()
String = []
#con = []
for i in s:
    String.append(i)
#    con.append(1)
#for i in range(0,len(String)):
#    for j in range(i+1,len(String)):
#        if String[i]==String[j] and String[i]!=0:
#            con[i] +=1
#            con[j] = 0 
subString = []
resString = []
for i in range(0,len(String)):
    subString.append(String[i:])
for i in range(0,len(subString)):
    resString.extend(diff(subString[i]))
resString.remove(s)     #得到所有子类字符串了
#去掉重复字符串
resString = list(set(resString))
resString.sort()   #妈的 千万千万别用冒泡排序 超级费时间
for i in range(0,len(resString)):
    if isLucky(resString[i]):
        print(resString[i])

#resulti = []
#result = []
#for l in range(0,len(resString)):
#    result.append(select(resString[l]))
#    resulti.append(0)
    
#for k in range(0,len(result)):
#    if result[k] == 0:
#        resulti[k]= k###
#result = remo(result,resulti)
#for i in range(0,len(resulti)):
#    if resulti[i]!=0:
#        result.remove(result[resulti[i]])
#rem = [0 for i in range(0,len(result))]
#for i in range(0,len(result)):
#    for j in range(i+1,len(result)):
#        if result[i] == result[j]:
#            result[j] = 0
#            rem[j] = j
#result = remo(result,rem)
#for i in range(0,len(result)):
#    if rem[i] ==1:
#        result.remove(result[i])
#result = paixu(result)           

#for i in range(0,len(result)):
#    print(result[i])

