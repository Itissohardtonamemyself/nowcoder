# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:45:25 2019

@author: LX

华为难题：栈 火车进站

"""

res = []
def find(a,b,c):
    if not a and not b:
        res.append(' '.join(map(str,c)))
    if b:
        c.append(b.pop())
        find(a,b,c)
        b.append(c.pop())
    if a:
        b.append(a.pop(0))
        find(a,b,c)
        a.insert(0,b.pop())

n = input()
n = int(n)
pre = list(map(int,input().split()))
ins,outs = [],[]
find(pre,ins,outs)
res.sort()
for i in res:
    print(i)

#data = []
#def find(x,y):
#    if len(x)==0:
#        return False
#    r = []
#    j = 0
#    for i in x:
#        r.append(i)
#        while j<len(y) and y[j]==r[-1]:
#            j+=1
#            r.pop()
#            if not r:
#                break
#    if r:
#        return False
#    return True
#def perm(l,st,end):
#    if st==end:
#        data.append(' '.join(map(str,l)))
#    else:
#        j = st
#        for i in range(st,end):
#            l[i],l[j] = l[j],l[i]
#            perm(l,st+1,end)
#            l[i],l[j] = l[j],l[i]
#
#n = input()
#n = int(n)
#s = [i for i in range(1,n+1)]
#lst = list(map(int,input().split()))
#perm(s,0,n)
#data.sort()
#for i in data:
#    if find(lst,list(map(int,i.split()))):
#        print(i)