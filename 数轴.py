# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 22:45:00 2018

@author: LX

数轴

"""

#n,s = map(int,input().split())
#lst = sorted(map(int,input().split()))
#end,start = max(lst[n-1]-s,lst[0]+s),min(lst[n-1]-s,lst[0]+s)
#for i in range(1,n-1):
#    if lst[i]+s>end and lst[i]-s<start:
#        if abs(lst[i]+s-start)>abs(end-(lst[i]-s)):
#            start = lst[i]-s
#        else:
#            end = lst[i]+s
#print(abs(end-start))

n,s = map(int,input().split())
lst = sorted(map(int,input().split()))
lit = [i-s for i in lst]
right,left =lit[n-1],lit[0]
if left+2*s>right:
    right = left+2*s
    left = lit[n-1]
diff = right-left
for i in range(1,n-1):
    if (lit[i]+2*s>right) and (lit[i]<left):
        if (lit[i]+2*s-left)>(right-lit[i]):
            right = lit[i]+2*s
        else:
            left = lit[i]
print(right-left)
