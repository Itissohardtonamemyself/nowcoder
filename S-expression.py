# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 10:37:19 2018

@author: LX

S-expression

"""
from functools import reduce
import math
def char2int(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def mulit_int(x,y):
    return 10*x+y

def str2int(s):
    if s.find('.')==-1:#不是浮点数
        return reduce(mulit_int,map(char2int,s))
    else:#是浮点数
        s1=s.split('.')
        s2int=reduce(mulit_int,map(char2int,s1[0])) #整数部分

        s2float=reduce(mulit_int,map(char2int,s1[1]))*0.1**len(s1[1]) #小数部分
        return s2int+s2float

def findright(elem,left,right):
    if left==right:
        return right
    if elem[left]=='(':
        sig = 1
    else:
        sig = 0
    i = left
    while sig!=0 and i<=right:
        i+=1
        if elem[i]=='(':
            sig+=1
        elif elem[i]==")":
            sig-=1
    return i

def cal(elem,left,right):
    if elem[left]=='(':
        if elem[left+1]=='if':
            sleft = left+2
            sright = findright(elem,sleft,right)
            s = cal(elem,sleft,sright)
            if s=='Type Mismatch' or s=='Division By Zero' or s=='Unbound Identifier':
                return s
            aleft = sright+1
            aright = findright(elem,aleft,right)
            bleft = aright+1
            bright = findright(elem,bleft,right)
            if s=='true':
                return cal(elem,aleft,aright)
            elif s == 'false':
                return cal(elem,bleft,bright)
            else:
                return 'Type Mismatch'
        elif elem[left+1]=='let':
            x = elem[left+3]
            aleft = left+4
            aright = findright(elem,aleft,right)
            a = cal(elem,aleft,aright)
            if a=='Type Mismatch' or a=='Division By Zero' or a=='Unbound Identifier':
                return a
            variable[x] = a#######
            bleft = aright+2
            bright = findright(elem,bleft,right)
            out = cal(elem,bleft,bright)
            if x in variable:
                variable.pop(x)
            return out
        op = elem[left+1]
        xleft = left+2
        xright = findright(elem,xleft,right)
        xRes = cal(elem,xleft,xright)
        if xRes == "Type Mismatch" or xRes == "Division By Zero" or xRes == "Unbound Identifier":
            return xRes
        yleft = xright+1
        yright = findright(elem,yleft,right)
        yRes = cal(elem,yleft,yright)
        if yRes=='Type Mismatch' or yRes=='Division By Zero' or yRes=='Unbound Identifier':
            return yRes
        if op=='/' and yRes=='0':
            return 'Division By Zero'
        if (not xRes[0].isdigit()) or (not yRes[0].isdigit()): ####
            return 'Type Mismatch'
        if op=='+':
            return str(str2int(xRes)+str2int(yRes))
        elif op=='-':
            return str(str2int(xRes)-str2int(yRes))
        elif op=='*':
            return str(str2int(xRes)*str2int(yRes))
        elif op=='/':
            if str2int(xRes)%str2int(yRes)==0:
                return str(str2int(xRes)//str2int(yRes))
            else:
                return str(str2int(xRes)/str2int(yRes))
        elif op=='<':
            if xRes<yRes:
                return "true"
            else:
                return 'false'
        elif op=='>':
            if xRes>yRes:
                return "true"
            else:
                return 'false'
        elif op=='=':
            if xRes==yRes:
                return "true"
            else:
                return 'false'
    elif elem[left][0].isdigit() or elem[left]=='true' or elem[left]=='false':
        return elem[left]
    elif elem[left]!='let' and elem[left]!='if':
        if elem[left] in variable:
            return variable[elem[left]]
        else:
            return 'Unbound Identifier'
    return 'Error'
variable = {}
n = input()
n = int(n)
for i in range(n):
    elem = input().split()
    print(cal(elem,0,len(elem)-1))


