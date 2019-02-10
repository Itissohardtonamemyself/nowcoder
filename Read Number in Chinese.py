# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:08:19 2018

@author: LX

function:Read Number in Chinese

"""
def change(a):
    if a == '1':
        a = 'yi'
    elif a == '2':
        a = 'er'
    elif a == '3':
        a = 'san'
    elif a == '4':
        a = 'si'
    elif a == '5':
        a = 'wu'
    elif a == '6':
        a = 'liu'
    elif a == '7':
        a = 'qi'
    elif a == '8':
        a = 'ba'
    elif a == '9':
        a = 'jiu'
    return a
out = ''
n = input()
num = []
for i in n:
    num.append(i)
if num[0]=='-':
    out = 'Fu '
    del num[0]
    
indexqian,indexyi = [],-1
leng = len(num)
for i in range(0,leng):
    if num[i]!='0':
        if leng - i==9:
            num[i] = change(num[i])+" Yi"
            indexyi = i
        elif leng -i==8 or leng -i==4:
            num[i] = change(num[i])+" Qian"
            indexqian.append(i)
        elif leng -i==7 or leng -i==3:
            num[i] = change(num[i])+" Bai"
        elif leng -i==6 or leng -i==2:
            num[i] = change(num[i])+" Shi"
        elif leng -i ==5:
            num[i] = change(num[i])+" Wan"
        else:
            num[i] = change(num[i])
indexwan = -1
for i in range(0,len(num)):
    if (leng - i ==5) and num[i]=='0':
        for j in range(i-1,-1,-1):
            if num[j]!='0':
                num[j] = num[j]+" Wan"
                indexwan = int(j)
                break
index = []
for i in range(0,leng):
    if num[i]!='0':
        index.append(i)
for i in range(0,len(index)-1):
    if index[i+1]-index[i]!=1:
        num[index[i]] = num[index[i]] + ' ling'
tem,st = [],''
if indexwan!=-1 and indexwan!=0 and len(indexqian)>0:
    for i in indexqian:
        if leng - indexwan>leng-i:
            tem = num[indexwan].split()
            tem.pop()
            st = ' '.join(tem)
            num[indexwan] = st
if indexyi!=-1:
    if len(indexqian)==1 and indexqian[0]-indexyi!=1:
        tem = num[indexyi].split()
        tem.pop()
        st=''
        st=' '.join(tem)
        num[indexyi] = st+" ling"  
indexwanwei = []
for i in range(1,leng):
    if leng-i>=5 and num[i]!='0':
        indexwanwei.append(i)
indexgewei = []
for i in range(1,leng):
    if leng-i<5 and num[i]!='0':
        indexgewei.append(i)
#100000090这种情况要提出来
if indexyi!=-1 and len(indexwanwei)==0 and len(indexgewei)>0:
    tem = num[indexyi].split()
    tem.pop()
    tem.pop()
    st=''
    st=' '.join(tem)
    num[indexyi] = st+" ling"  
if indexyi!=-1 and len(indexwanwei)==0 and len(indexgewei)==0:
    tem = num[indexyi].split()
    tem.pop()
    st=''
    st=' '.join(tem)
    num[indexyi] = st 
cnt = 0
for i in num:
    if i=='0':
        cnt+=1
for i in range(0,cnt):
    num.remove('0')
if num:
    print(out+" ".join(num))
else:
    print("ling")