# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 19:34:21 2018

@author: LX

锤子剪刀布

"""

def vs(a,b):
    if a=='C' and b=='J':
        return True,False,'C'
    elif a=='C' and b=='B':
        return False,True,'B'
    
    elif a=='J' and b=='B':
        return True,False,'J'
    elif a=='J' and b=='C':
        return False,True,'C'
    
    elif a=='B' and b=='C':
        return True,False,'B'
    elif a=='B' and b=='J':
        return False,True,'J'
    else:
        return -1,-1,'o'
    
n = input()
n = int(n)
jias,jiap,jiaf,yis,yip,yif,jia,yi = 0,0,0,0,0,0,-1,-1
jiac,jiaj,jiab,yic,yij,yib=0,0,0,0,0,0
for i in range(0,n):
    j,y = map(str,input().split())
    jia,yi,st = vs(j,y)
    if jia==-1:
        jiap+=1
    elif jia:
        jias+=1
        if st=='C':
            jiac+=1
        elif st=='J':
            jiaj+=1
        else:
            jiab+=1
    else:
        jiaf+=1
    if yi==-1:
        yip+=1
    elif yi:
        yis+=1
        if st=='C':
            yic+=1
        elif st=='J':
            yij+=1
        else:
            yib+=1
    else:
        yif+=1
if jiab>=jiac and jiab>=jiaj:
      jiaout = 'B'
elif jiac>=jiaj and jiac>jiab:
      jiaout = 'C'
else:
      jiaout = 'J'
if yib>=yic and yib>=yij:
      yiout = 'B'
elif yic>=yij and yic>yib:
      yiout = 'C'
else:
      yiout = 'J'     
print(str(jias)+" "+str(jiap)+" "+str(jiaf))
print(str(yis)+" "+str(yip)+" "+str(yif))
print(jiaout+" "+yiout)    