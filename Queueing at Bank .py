# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:13:02 2018

@author: LX

Queueing at Bank 

"""


#def tcmp(a,b):
#	if a > b :
#		return -1
#	elif a < b :
#		return 1
#	else:
#		return 0
#		
#nums = [1,2,3,4]
#sorted_nums = sorted(nums, key = functools.cmp_to_key(tcmp))

#from queue import Queue
#import functools


import queue
import operator

class Customer:
    def __init__(self,arrivingTime,processingTime,index):
        self.arrivingTime = arrivingTime
        self.processingTime = processingTime
        self.index = index
        self.waitingTime = 0
class Timeunit:
    def __init__(self,time,isCustomer,index=0):
        self.time = time
        self.isCustomer = isCustomer
        self.index = index
    def __lt__(self,other):
       return operator.lt(self.time,other.time)  #cmp(self.time,other.time)

start,end = 8*3600,17*3600
Timeline = queue.PriorityQueue()
n,m = map(int,input().split())
lst = []
index = 0
for i in range(n):
    tem,posstem = map(str,input().split())
    tem = list(map(int,tem.split(":")))
    arrivtem = tem[0]*3600+tem[1]*60+tem[2]
    if arrivtem<=end:
        posstem = int(posstem)*60
        lst.append(Customer(arrivtem,posstem,index))
        Timeline.put(Timeunit(arrivtem,True,index))
        index+=1
waitinglist = []
i,k,N = 0,0,len(lst)
while k<m:
    Timeline.put(Timeunit(start,False))
    k+=1
while i<N:
    item = Timeline.get()
    if item.isCustomer:
        if k<m:
            k+=1
            lst[item.index].waitingTime=item.time - lst[item.index].arrivingTime
            i+=1
            Timeline.put(Timeunit(item.time+lst[item.index].processingTime,False))
        else:
            waitinglist.append(item.index)
    else:
        if waitinglist:
            index = waitinglist.pop(0)
            lst[index].waitingTime = item.time-lst[index].arrivingTime
            i+=1
            Timeline.put(Timeunit(item.time+lst[index].processingTime,False))
        else:
            k-=1
sa = 0
for item in lst:
    sa+=item.waitingTime
out = "%.1f"%(sa/(N*60))
print(out)

