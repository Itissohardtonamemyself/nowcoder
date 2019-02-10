
"""
Created on Sun Nov  4 12:57:07 2018

@author: LX
"""

a = input().split()
A = a[0]
da = a[1]
ma = ""
B = a[2]
db = a[3]
mb = ''
filter(str.isdigit, A)
filter(str.isdigit, B)
for i in A:
    if da == i:
       ma = ma +da 
for i in B:
    if i==db:
        mb = mb + db
#去除非数字字符串
filter(str.isdigit, ma)
filter(str.isdigit, mb)
output = int(ma)+int(mb)
print(output)

#a, b, c, d = input().split()
# 
#print(int(a.count(b) * b or "0") + int(c.count(d) * d or "0"))
