# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:27:08 2018

@author: wentong

function:pop sequence

"""
#def boo(tlst):
#  stack = list(num[:tlst[0]])
#  out = []
#  if len(stack)>m:
#         return False
#  elif len(tlst)>=3:
#      out.append(stack.pop())
#      if tlst[0]>1 and tlst[0]<n:
#          a,b = tlst[0]+1,tlst[0]-1 
#          for i in range(1,len(tlst)):
#              if tlst[i]==a and tlst[i]<n:
#                  out.append(tlst[i])
#                  a = tlst[i]+1
#              elif tlst[i]==b:
#                  out.append(tlst[i])
#                  b = tlst[i]-1
#                  stack.pop()
#              elif tlst[i]==a:
#                  stack = sorted(set(num)-set(out))
#                  if len(stack)>m:
#                      return False
#                  out.append(stack.pop())
#              else:
#                  return False
#      elif tlst[0]==1 and tlst[1]==n:
#            stack = list(num[1:tlst[1]])
#            if len(stack)>m:
#                return False
#            out.append(stack.pop())
#            a,b = tlst[3]+1,tlst[3]-1 
#            for i in range(2,len(tlst)):
#              if tlst[i]==a and tlst[i]<n:
#                  out.append(tlst[i])
#                  a = tlst[i]+1
#              elif tlst[i]==b and tlst[i]>1:
#                  out.append(tlst[i])
#                  b = tlst[i]-1
#                  stack.pop()
#              elif tlst[i]==a:
#                  stack = sorted(set(num)-set(out))
#                  if len(stack)>m:
#                      return False
#                  stack.pop()
#              else:
#                  return False
#      elif tlst[0]==1 and tlst[1]<n:
#          a,b = tlst[1]+1,tlst[1]-1 
#          for i in range(2,len(tlst)):
#              if tlst[i]==a and tlst[i]<n:
#                  out.append(tlst[i])
#                  a = tlst[i]+1
#              elif tlst[i]==b and tlst[i]>1:
#                  out.append(tlst[i])
#                  b = tlst[i]-1
#                  stack.pop()
#              elif tlst[i]==a:
#                  stack = sorted(set(num)-set(out))
#                  if len(stack)>m:
#                      return False
#                  stack.pop()
#              else:
#                  return False
#      elif tlst[0]==n and tlst[1]==n-1:
#           stack = list(num)
#           if len(stack)>m:
#               return False
#           else:
#              out.append(stack.pop())
#              out.append(stack.pop())
#              a,b = tlst[1]+1,tlst[1]-1 
#              for i in range(2,len(tlst)):
#                  if tlst[i]==a and tlst[i]<n:
#                      out.append(tlst[i])
#                      a = tlst[i]+1
#                  elif tlst[i]==b and tlst[i]>1:
#                      out.append(tlst[i])
#                      b = tlst[i]-1
#                      stack.pop()
#                  elif tlst[i]==a:
#                      stack = sorted(set(num)-set(out))
#                      if len(stack)>m:
#                          return False
#                      stack.pop()
#                  else:
#                      return False           
#      else:
#          return False
#  else:
#       return True
#  return True
m,n,k = map(int,input().split())
num = [i for i in range(1,n+1)]
for i in range(0,k):
    tem = list(map(int,input().split()))
    stack = []
    out,count = True,0
    for j in range(1,n+1):
        stack.append(j)
        if len(stack)>m:
            out = False
            break
        while len(stack)!=0 and stack[len(stack)-1]==tem[count]:
            stack.pop()
            count = count + 1
    if out and len(stack)==0:
        print("YES")
    else:
        print("NO")
  




