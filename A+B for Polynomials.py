# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:41:12 2018

@author: wentong

fucntion:A+B for Polynomials

"""
lsa = list(map(float,input().split()))
lsb = list(map(float,input().split()))
a,b = 0,0
lsta,lstb = [],[]
for i in range(int(lsa[0])-1,-1,-1):
    lsta.append([lsa[2+2*i],int(lsa[1+2*i])])
for i in range(int(lsb[0])-1,-1,-1):
    lstb.append([lsb[2+2*i],int(lsb[1+2*i])])
for i in range(0,lsta[len(lsta)-1][1]):
    if lsta[i][1]!=i:
        lsta = lsta[:i]+[[0,0]]+lsta[i:]
for i in range(0,lstb[len(lstb)-1][1]):
    if lstb[i][1]!=i:
        lstb = lstb[:i]+[[0,0]]+lstb[i:]
leng = min(len(lsta),len(lstb))
t = 0
out = []
for i in range(0,leng):
    t = lsta[i][0]+lstb[i][0]
#    if t>=10:
#        t = t-10
#        lsta[i+1][0] +=1
    out.append([t,i])
#t = lsta[leng-1][0]+lstb[leng-1][0]
#if t>=10:
#    t = t - 10
#    if len(lsta)>len(lstb):
#        lsta[leng][0]+=1
#        out.append([t,leng-1])
#    elif len(lsta)<len(lstb):
#        lstb[leng][0]+=1
#        out.append([t,leng-1])
#    else:
#        out.append([t,leng-1])
#        out.append([1,leng])
if len(lsta)>len(lstb):
    for i in range(leng,len(lsta)):
#        if lsta[i][0]>=10:
#            lsta[i][0] = lsta[i] - 10
#            lsta[i+1][0] +=1
        out.append(lsta[i])
else:
    for i in range(leng,len(lstb)):
#        if lstb[i][0]>=10:
#            lstb[i][0] = lstb[i] - 10
#            lstb[i+1][0] +=1
        out.append(lstb[i])
cnt = 0
for i in out:
    if i[0]!=0:
        cnt+=1
print(str(cnt)+" ",end='')
for i in range(len(out)-1,0,-1):
    if out[i][0]!=0:
        tem = []
        for k in str(out[i][0]):
            tem.append(k)
        if len(tem)<=7:
            print(str(out[i][1])+" "+str(out[i][0])+" ",end='')
        else:
            t = "%.1f"%out[i][0]
            print(str(out[i][1])+" "+t+" ",end='')
if out[0][0]!=0:
    tem = []
    for k in str(out[i][0]):
        tem.append(k)
    if len(tem)<=7:
        print(str(out[0][1])+" "+str(out[0][0])+" ",end='')
    else:
        t = "%.1f"%out[0][0]
        print(str(out[0][1])+" "+t+" ",end='')
        
