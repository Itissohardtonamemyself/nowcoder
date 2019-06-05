# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 23:04:00 2018

@author: LX

1071. Speech Patterns 

"""
import re
from collections import Counter
lst = []
word=re.findall('[0-9a-z]+',input().lower())
c = Counter(word).items()
m = max(c,key=lambda x:x[1])[1]
for i in c:
    if i[1]==m:
        lst.append(list(i))
lst.sort(key=lambda x:(x[0]))
print(lst[0][0]+" "+str(lst[0][1]))

