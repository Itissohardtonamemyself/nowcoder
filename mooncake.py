# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:06:55 2018

@author: LX

function: dongtaiyouhua

"""
while True:
    try:
        lst2,lst3,N,D=[],[],0,0
        N,D = map(int,input().strip().split())
        lst2 = list(map(float,input().strip().split()))
        lst3 = list(map(float,input().strip().split()))
        dan = []
        dani = []
        su = 0.0
        
        for i in range(0,N):
            try:
                dan.append(lst3[i]/lst2[i])
                dani.append(i)
            except:
                dan[i]=0
        for i in range(0,len(dan)-1):
            for j in range(0,len(dan)-i-1):
                if dan[j]<dan[j+1]:
                    dan[j],dan[j+1] = dan[j+1],dan[j]
                    dani[j],dani[j+1] = dani[j+1],dani[j]
        for i in range(0,len(dan)):
            if D>=lst2[dani[i]]:
                D = D - lst2[dani[i]]
                su = su + lst3[dani[i]] 
            else:
                su = su + (lst2[dani[i]]-D) * dan[i]
                break
        print("%.2f"%su)
    except:
        break
  

#import operator
#while True:
#    try:
#        N,D = map(int,input().strip().split())
#        list_stock = list(map(float,input().strip().split()))
#        list_price = list(map(float,input().strip().split()))
#        dict1 = {}
#        for i in range(N):
#            try:
#                dict1[i] = list_price[i]/list_stock[i]
#            except:
#                dict1[i] = 0
#        dict2 = sorted(dict1.items(), key=operator.itemgetter(1),reverse=True)#按照元素排序,生成存储元组的列表
#        price = 0
#        for j in dict2:
#            type_c = j[0]
#            price_c = j[1]
#            num_stock = list_stock[type_c]
#            if D == 0 or price_c == 0:
#                break
#            elif D >= num_stock:
#                price += list_price[type_c]
#                D -= num_stock
#            else:
#                price += D * price_c
#                break
#        print("%.2f" %price)
#    except:
#        break