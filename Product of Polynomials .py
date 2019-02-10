# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:29:52 2018

@author: LX

Product of Polynomials 

"""

n,out = [],[]
n1 = list(map(float,input().split()[1:]))
n2 = list(map(float,input().split()[1:]))
for i in range(0,len(n1),2):
    for j in range(0,len(n2),2):
        n.append([int(n1[i]+n2[j]),n1[i+1]*n2[j+1]])
n.sort(key=lambda x:(-x[0]))
sa,co = n[0][1],n[0][0]
for i in n[1:]:
    if i[0]==co:
        sa+=i[1]
    else:
        te=str(sa)
        if len(te[te.index('.'):])>=3 and te[te.index('.')+2]=='5' and sa>0:
            out.extend([str(co),'%.1f'%(sa+0.01)])
        elif len(te[te.index('.'):])>=3 and te[te.index('.')+2]=='5' and sa<0:
            out.extend([str(co),'%.1f'%(sa-0.01)])
        else:
            out.extend([str(co),'%.1f'%sa])
        sa=i[1]
        co=i[0]
te=str(sa)
if len(te[te.index('.'):])>=3 and te[te.index('.')+2]=='5' and sa>0:
    out.extend([str(co),'%.1f'%(sa+0.01)])
elif len(te[te.index('.'):])>=3 and te[te.index('.')+2]=='5' and sa<0:
            out.extend([str(co),'%.1f'%(sa-0.01)])
else:
    out.extend([str(co),"%.1f"%sa])
le = len(out)//2
print(le,' '.join(out))


#n,out = [],[]
#n1 = list(map(float,input().split()[1:]))
#n2 = list(map(float,input().split()[1:]))
#for i in range(0,len(n1),2):
#    for j in range(0,len(n2),2):
#        n.append([int(n1[i]+n2[j]),n1[i+1]*n2[j+1]])
#n.sort(key=lambda x:(-x[0]))
#sa,co = n[0][1],n[0][0]
#for i in n[1:]:
#    if i[0]==co:
#        sa+=i[1]
#    else:
#        out.extend([str(co),'%.1f'%sa])
#        sa=i[1]
#        co=i[0]
#out.extend(str(co),"%.1f"%sa)
#le = len(out)//2
#print(le,' '.join(out))