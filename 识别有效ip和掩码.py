# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:10:54 2019

@author: LX

识别有效ip和掩码

"""

A = ['001000000000','126255255255']
s1 = ['010000000000','010255255255']

B = ['128000000000','191255255255']
s2 = ['172016000000','172031255255']

C = ['192000000000','223255255255']
s3 = ['192168000000','192168255255']

D = ['224000000000','239255255255']
E = ['240000000000','255255255255']

outlst = [0]*7

def two(y):
    o = ''
    if y>0:
        while y>0:
            o = str(y%2)+o
            y = y//2
        return '%08d'%int(o)
    else:
        return '00000000'

def iswyan(x):
    if x == '255.255.255.255' or x == '0.0.0.0':
        return True
    t = x.split('.')
    if len(t)!=4:
        return True
    st = ''
    for i in t:
        st = st + two(int(i))
    for i in range(32):
        if st[i]=='0':
            for j in range(i+1,32):
                if st[j]=='1':
                    return True
    return False
    
def iswip(x):
    t = x.split('.')
    if len(t)!=4:
        return True
    for i in t:
        if len(i)==0:
            return True
    return False
    
def t(x):
    tmp = list(map(int,x.split('.')))
    out = ''
    for i in range(4):
        out = out+'%03d'%tmp[i]
    return out

try:
    while True:
        s = input()
        if s=='':
            break
        s = s.split('~')
        if iswyan(s[1]):
            outlst[5]+=1
        elif iswip(s[0]):
            outlst[5]+=1
        else:
            ip = t(s[0])
            if ip>=A[0] and ip<=A[1]:
                outlst[0]+=1
                if ip>=s1[0] and ip<=s1[1]:
                    outlst[6]+=1
            elif ip>=B[0] and ip<=B[1]:
                outlst[1]+=1
                if ip>=s2[0] and ip<=s2[1]:
                    outlst[6]+=1
            elif ip>=C[0] and ip<=C[1]:
                outlst[2]+=1
                if ip>=s3[0] and ip<=s3[1]:
                    outlst[6]+=1
            elif ip>=D[0] and ip<=D[1]:
                outlst[3]+=1
            elif ip>=E[0] and ip<=E[1]:
                outlst[4]+=1
except:
    pass
print(' '.join(map(str,outlst)))