# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:40:13 2018

@author: LX

function:给定一个正整数数列，和正整数p，设这个数列中的最大值是M，最小值是m，如果M <= m * p，则称这个数列是完美数列。

现在给定参数p和一些正整数，请你从中选择尽可能多的数构成一个完美数列。

"""
#由于复杂度过大 需要更新算法 
    
#def panduanxiao(a,cont):
#    for i in range(0,len(lst)):
#        M = lst[len(lst)-i-1]
#        m = lst[cont]
#        if M<=m*p:
#            return True
#        else:
#            return False
#def panduanda(a,cont):
#    for i in range(0,len(lst)):
#        M = lst[len(lst)-1-cont]
#        m = lst[i]
#        if M<=m*p:
#            return True
#        else:
#            return False
def erfen(a):
    count1 = 0
    count2 = len(lst)-1
    while count1<=count2:
        middle = int(count1+(count2-count1)/2)
        if lst[middle]>a:
            count2 = middle - 1
        else:
            count1 = middle + 1
    return count2
n,p = map(int,input().strip().split())
lst = list(map(int,input().strip().split()))
lst.sort()
lst1 = []
for i in range(0,len(lst)):
    lst1.append(lst[i]*p)
#用二分法查找
lst2 = []
for i in range(0,len(lst)):
    lst2.append(erfen(lst1[i])-i+1)
res = max(lst2)
print(res)

#boo,boo1 = False,False
#while boo==False:
#    boo = panduanxiao(lst,count1)
#    count1+=1  
#while boo1==False:
#    boo1 = panduanda(lst,count2)
#    count2+=1
#con = min(count1-1,count2-1)
#print(len(lst)-con)


#for i in range(0,len(lst)):
#    for j in range(i,len(lst)):
#        if lst[j]<=lst[i]*p and lst[j]>=lst[i]:
#             if ma<j-i+1:
#                 ma = j-i+1



#n,p = map(int,input().split())
#lst = list(map(int,input().split()))
#lst.sort()
##以序列中最小的为准，找最大
##以序列中最大的为准，找最小
#max1 = 0
#for i in range(n):
#    for j in range(i+max1,n):
#        if lst[j] > lst[i]*p:
#            break
#        max1+=1
#print(max1)

#max2 = 0
#for i in range(n-1,-1,-1):
#    for j in range(n-1,i-1-max2,-1):
#        if lst[i] > lst[j]*p:
#            break
#        max2 += 1    




