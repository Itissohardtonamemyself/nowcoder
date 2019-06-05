# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:36:11 2018

@author: LX

function link: https://www.nowcoder.com/pat/6/problem/4045

"""

def bubble_sort_min(nums):
    for i in range(len(nums) - 1):  
        for j in range(len(nums) - i - 1):  
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
def bubble_sort_max(nums):
    for i in range(len(nums) - 1): 
        for j in range(len(nums) - i - 1):  
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
def waca(de):
    N =  de
    ma1 = []
    mi1 = []
    mao1 = 0
    mio1 = 0
    for i in N:
        ma1.append(i)
        mi1.append(i)
        ma1 = bubble_sort_max(ma1)
        mi1 = bubble_sort_min(mi1)

    ma1= list(map(int,ma1))
    mi1 = list(map(int,mi1))
    
    for i in range(len(ma1)):
        mao1 = (10**(len(ma1)-i-1))*ma1[i]+ mao1
    for i in range(len(mi1)):
        mio1 = (10**(len(mi1)-i-1))*mi1[i]+ mio1
    defnum = mao1-mio1
    output(mao1,mio1,defnum)
    return str(defnum)
def outstr(n):
    n1 = ''
    if n==0:
        n1 = "0000"
    elif n<10:
        n1 = "000"+str(n)
    elif n<100:
        n1 = "00" + str(n)
    elif n<1000:
        n1 = "0"+str(n)
    else:
        n1 = str(n)
    return n1

def output(a,b,c):
    a1,b1,c1='','',''
    a1 = outstr(a)
    b1 = outstr(b)
    c1 = outstr(c)      
    print(a1+" - "+b1+" = "+c1)

de = input()
de = outstr(int(de))
de = waca(de)    
while(de!="0" and de!="6174"):
    de = outstr(int(de))
    de = waca(de)
    
