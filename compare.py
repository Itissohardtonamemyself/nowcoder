# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:09:26 2018

@author: LWT

version1 简单遍历
"""
#a**3==b**3+c**3+d**3
#input n   n>1 n<=100 
count =0 #复杂度
print "请输入n:"
n = input()
n = int(n)
if n>0 and n<=100:
    for b in range(1,n+1): #abcd中总有最小值 设b为最小值
        for c in range(b+1,n+1):
            for d in range(c+1,n+1):
                for a in range(d+1,n+1):
                    count +=1
                    if a**3==(b**3+c**3+d**3):
                        print "输出结果a，b，c，d分别是："+str(a)+" "+str(b)+" "+str(c)+" "+str(d) 
else:
    print "输入太大了"

print "复杂度是："+str(count)
    

