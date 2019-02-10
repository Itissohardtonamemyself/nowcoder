# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 09:47:37 2018

@author: 1
"""

import random

width = 800
height = 600
X = []
Y = []
temp = 0.0
count1 = 0
count2 = 0
conmov = 0
panch = False
pansqr = False

def randmax(a,temp):
    if a>temp:
        temp = a
    
    return temp

def ischangfang(x1,y1,x2,y2,ma,count1):
    while count1 < 2:
        if pow(((x2-x1)**2)*((y2-y1)**2),0.5) == ma:
            count1 += 1
    if count1 == 2:
        count1 = 0
        return True

def issqr(x1,y1,x2,y2,ma,count2):
    while count2 < 3:
        if pow(((x2-x1)**2)*((y2-y1)**2),0.5) != ma:
            count2 += 1   
    if count2 == 3:
        count2 = 0
        return True
    
def moving(a,b,a1,b1):
        a1 = a + (b-b1)
        b1 = b - (a-a1)  
        return a1,b1

print "请输入你想解决的杂物个数："
n = int(input())
for i in range(0,n):
    
    a = random.randint(0,width)
    b = random.randint(0,height)
    
    for j in range(0,4):
        x = random.randint(0,width)
        X.append(x)
        y = random.randint(0,height)
        Y.append(y)    
  
    print "杂物"+str(i+1)+"初始点为:\r\n"
    for i in range(0,4):
        print "点"+str(i+1)+"的横坐标为: "+str(X[i])+"纵坐标为: "+str(Y[i])+"\r\n"    
    
    for i in range(0,4):
        for j in range(i,4):
            tem = randmax(pow(((X[i]-X[j])**2)*((Y[i]-Y[j])**2),0.5),temp)
    for i in range(0,4):
        for j in range(i,4):
            panch = ischangfang(X[i],Y[i],X[j],Y[j],tem,count1)  
    if panch:
        for i in range(0,4):
            for j in range(i,4):
                pansqr = issqr(X[i],Y[i],X[j],Y[j],tem,count2)
                if pansqr:
                    continue
            if pansqr:
                continue
    
    
    if pansqr!=True:
        for i in range(0,4):
            X[i],Y[i] = moving(a,b,X[i],Y[i])
            conmov += 1
        #作移动操作
            for i in range(0,4):
                for j in range(i,4):
                    tem = randmax(pow(((X[i]-X[j])**2)*((Y[i]-Y[j])**2),0.5),temp)
            for i in range(0,4):
                for j in range(i,4):
                    panch = ischangfang(X[i],Y[i],X[j],Y[j],tem,count1)
            if panch:
                for i in range(0,4):
                    for j in range(i,4):
                        pansqr = issqr(X[i],Y[i],X[j],Y[j],tem,count2)
                        if pansqr:
                            continue
                    if pansqr:
                        continue
                if pansqr:
                    continue
            else:
                pansqr = False
          
            if i==3:
                 a = random.randint(0,width)
                 b = random.randint(0,height)
      
    #显示最终结果
    print "杂物"+str(i+1)+"的最终结果为:\r\n"
    print "移动次数为："+str(conmov)
    print "小人操作的点坐标为x: "+str(a)+"y: "+str(b)+"\r\n"
    for i in range(0,4):
        print "点"+str(i+1)+"的横坐标为: "+str(X[i])+"纵坐标为: "+str(Y[i])+"\r\n"
  
    

    