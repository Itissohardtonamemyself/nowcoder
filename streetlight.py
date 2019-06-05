# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 12:02:20 2018

@author: LX
"""
tem = ""
arr = []
boo = []
pos = []
count = 0

def domath(count,array,pos,boo):
    for i in range(0,len(array)):
        if boo[i]:
            if array[i] == 1:
                count += 1
                pos.append(i+1)
                boo[i],boo[i+1],boo[i+2]=False,False,False
        else:
            continue
    return count,array,pos,boo

print("请输入路长度：")
a = input()
a = int(a)
for i in range(0,a):
    arr.append(0)
    boo.append(True)

print("请输入你想照亮的地方的个数：")
b = input()
b = int(b)
for i in range(0,b):
    print("请输入你想照亮的第"+str(i+1)+"地方: ")
    tem = input()
    tem = int(tem)
    if tem>(len(arr)-1):
        print("超出长度")
        break
    else:
        arr[tem] = 1

if len(arr)%3==0:
    count,arr,pos,boo=domath(count,arr,pos,boo)
if len(arr)%3==1:
    if arr[len(arr)-1]==1:
        count += 1
        arr.pop()
        count,arr,pos,boo=domath(count,arr,pos,boo)
        pos.append(len(arr)-1)
    else:
        arr.pop()
        count,arr,pos,boo=domath(count,arr,pos,boo)
if len(arr)%3==2:
    if arr[len(arr)-1]==1 or arr[len(arr)-2]==1:
        count += 1
        arr.pop()
        arr.pop()
        count,arr,pos,boo=domath(count,arr,pos,boo)
        pos.append(len(arr)-1)
    else:
        arr.pop()
        arr.pop()
        count,arr,pos,boo=domath(count,arr,pos,boo)

print("最终结果是：")
print(pos)           
print("路灯有："+str(count)+"个")

    
    

