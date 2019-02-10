# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:05:04 2018

@author: wentong

"""
array = [[1,2,3],[4,5,6],[7,8,9]]
target = 3
for i in range(0,len(array)):
    for j in range(0,len(array[i])):
        if target == array[i][j]:
            print("True")
            break
        elif i==len(array)-1 and j ==len(array[i])-1 :
            print("False")

