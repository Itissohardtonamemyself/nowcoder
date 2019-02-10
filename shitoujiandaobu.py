# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:42:22 2018

@author: LX
"""

N = input()
N = int(N)
js,jp,jf = 0,0,0
ys,yp,yf = 0,0,0
jsheng = []
ysheng = []
J = ''
Y = ''
res = []
for i in range(0,N):
    res.append(list(input().split()))
for i in range(0,N):
    if (res[i][0] =='C' and res[i][1] =='J') or (res[i][0] =='J' and res[i][1] =='B') or(res[i][0] =='B' and res[i][1] =='C'):
        js += 1
        yf += 1
        jsheng.append(res[i][0])
    elif (res[i][0] =='C' and res[i][1] =='C') or (res[i][0] =='J' and res[i][1] =='J') or(res[i][0] =='B' and res[i][1] =='B'):
        jp += 1
        yp += 1
    elif (res[i][0] =='C' and res[i][1] =='B') or (res[i][0] =='J' and res[i][1] =='C') or(res[i][0] =='B' and res[i][1] =='J'):
        jf += 1
        ys += 1
    elif (res[i][1] =='C' and res[i][0] =='J') or (res[i][1] =='J' and res[i][0] =='B') or(res[i][1] =='B' and res[i][0] =='C'):
        ys += 1
        jf += 1
        ysheng.append(res[i][1])
    elif (res[i][1] =='C' and res[i][0] =='C') or (res[i][1] =='J' and res[i][0] =='J') or(res[i][1] =='B' and res[i][0] =='B'):
        yp += 1
        jp += 1
    elif (res[i][1] =='C' and res[i][0] =='B') or (res[i][1] =='J' and res[i][0] =='C') or(res[i][1] =='B' and res[i][0] =='J'):
        yf += 1
        js += 1

if jsheng.count('C')== 0 and jsheng.count('J')==0 and jsheng.count('B')==0:
    J = 'B'
else:
     if max(jsheng.count('C'),jsheng.count('J'),jsheng.count('B'))==jsheng.count('B'):
         J = 'B' 
     elif max(jsheng.count('C'),jsheng.count('J'),jsheng.count('B'))==jsheng.count('C'):
         J = 'C'
     elif max(jsheng.count('C'),jsheng.count('J'),jsheng.count('B'))==jsheng.count('J'):
         J = 'J'
      
    
if ysheng.count('C')==0 and ysheng.count('J')==0 and ysheng.count('B')==0:
    Y = 'B'
else: 
     if max(ysheng.count('C'),ysheng.count('J'),ysheng.count('B'))==ysheng.count('B'):
         Y = 'B'
     elif max(ysheng.count('C'),ysheng.count('J'),ysheng.count('B'))==ysheng.count('C'):
         Y = 'C'
     elif max(ysheng.count('C'),ysheng.count('J'),ysheng.count('B'))==ysheng.count('J'):
         Y = 'J'
      

print("%d %d %d"%(js,jp,jf),end="\n")
print("%d %d %d"%(ys,yp,yf),end="\n")
print(J+" "+Y)

