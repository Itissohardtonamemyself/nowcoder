# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:05:05 2018

@author: LX

To Fill or Not to Fill 

"""

cmax,d,davg,n = map(int,input().split())
lst1 = []
dis = cmax*davg
for i in range(n):
    tem = input().split()
    lst1.append([float(tem[0]),int(tem[1])])
lst1.sort(key = lambda x:(x[1],x[0]))
k = lst1[0][1]
lst = [lst1[0]]
for i in lst1:
    if k!=i[1]:
        lst.append(i)
        k = i[1]
lst.sort(key = lambda x:(x[1],x[0]))
i,j,price,travel,boo,cleft = 0,1,0.0,0,True,0
while j<len(lst) and i<len(lst)-1 and d>0:
    mi,boo1,tem1 = lst[i][0],False,[]  
    if lst[j][1]-lst[i][1]>dis:
            print("The maximum travel distance = "+str("%.2f"%(travel+dis)))
            boo= False
            break
    while j<len(lst) and i<len(lst)-1 and lst[j][1]-lst[i][1]<=dis:
         if lst[j][0]<mi:
            mi = lst[j][0]
            boo1 = True
            te = lst[j]
            break
         temp = list([j]+lst[j])
         tem1.append(temp) 
         j+=1
#        if j==n:
#            break
    if boo1:
#        if d-(te[1]-lst[i][1])>0:
    
#        else:
#            break
        if cleft<=te[1]-lst[i][1]:
            price += lst[i][0]*(te[1]-lst[i][1]-cleft)/dis*cmax
            cleft = 0
        else:
            cleft -=te[1]-lst[i][1]       
        travel+=(te[1]-lst[i][1])
        d-=(te[1]-lst[i][1])
        if j<len(lst):
            i = int(j)
        else:
            break
#        if i>=n-1:
#            break
        j = i+1
        if j==len(lst):
            break
        if lst[j][1]-lst[i][1]>dis:
            print("The maximum travel distance = "+str("%.2f"%(travel+dis)))
            boo= False
            break
    else:
#        if d-(lst[j-1][1]-lst[i][1])>0:
        
#        else:
#            break
        if d>dis:
            tem1.sort(key=lambda x:(x[1]))
            price += lst[i][0]*(dis-cleft)/dis*cmax       
            travel+=(tem1[0][2]-lst[i][1])
            cleft = dis - (tem1[0][2]-lst[i][1])
            d-=(tem1[0][2]-lst[i][1])
            i = int(tem1[0][0])
            j = i+1
        else:
            price+=lst[i][0]*(d-cleft)/dis*cmax
            travel+=d
            d-=(lst[j-1][1]-lst[i][1])
            cleft = d
            i = int(j-1)
            j=i+1
        
if boo:
    price = price+(d-cleft)/dis*cmax*lst[i][0]
    print("%.2f"%price)        
#while d>0 and j<n and i<n-1 and boo:
##    tem = []
#    while j<n and i<n-1 and lst[j][1]-lst[i][1]<=dis:
#        if lst[j][0]<lst[i][0]:
#            price+=lst[i][0]*(lst[j][1]-lst[i][1])/dis*cmax
#            d-=(lst[j][1]-lst[i][1])
#            tra+=(lst[j][1]-lst[i][1])
#            i = int(j)
#            if i==n-1:
#                break
#            j = i+1
#            if lst[j][1]-lst[i][1]>dis:
#                print("The maximum travel distance = "+str(tra))
#                boo= False
#                break
##            if j==n:
##                break
#        else:
##            j+=1
##            if j==n:
##                break
#            if lst[j][1]-lst[i][1]>dis:
##                j-=1
##                price+=lst[i][0]*(lst[j][1]-lst[i][1])/dis*cmax
##                d-=(lst[j][1]-lst[i][1])
##                tra+=(lst[j][1]-lst[i][1])
##                i = int(j)
###                if i==n-1:
###                    break
##                j = i+1
##                if lst[j][1]-lst[i][1]>dis:
#                    print("The maximum travel distance = "+str(tra))
#                    boo= False
#                    break
#            else:
#                t = int(i)
#                while j<n and i<n-1 and lst[j][1]-lst[i][1]<=dis and lst[j][0]<=lst[t][0]:
#                    t = int(j)
#                    j+=1
#                price+=lst[i][0]*(lst[j][1]-lst[i][1])/dis*cmax
#                d-=(lst[j][1]-lst[i][1])
#                tra+=(lst[j][1]-lst[i][1])
#                i = int(j)
#                if i==n-1:
#                    break
#                j = i+1
##        if j==n:
##            break
##        temp = list(lst[j])
##        temp.append(j)
##        tem.append(temp)
##        j+=1
##        if j==n:
##            break
##    if tem:    
##        tem.sort(key=lambda x:(x[0]))
##        price+=lst[i][0]*(-lst[i][1]+tem[0][1])/dis*cmax
##        d -=(-lst[i][1]+tem[0][1])
##        tra+=(-lst[i][1]+tem[0][1])
##        i = int(tem[0][2])
##        if i==n-1:
##            break
##        j=i+1
##    else:
##        print("The maximum travel distance = "+str(tra))
##        boo = False
##        break
#if boo:
#    price = price+d/dis*cmax*lst[i][0]
#    print("%.2f"%price)
     
        
    

