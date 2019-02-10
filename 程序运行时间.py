# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 13:00:30 2018

@author: LX

程序运行时间

"""

n1,n2 = map(int,input().split())
te = '%.1f'%((n2-n1)/100)
sec = int('%d'%((n2-n1)/100))
if te[-1]=='5':
    sec+=1
hour = "%02d"%(sec//3600)
minute = "%02d"%(sec%3600//60)
sec = "%02d"%(sec%3600%60)
print(hour+":"+minute+":"+sec)
