# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:57:05 2022

@author: 406429
"""

N,M = map(int, input().split())

B = [0]*100009

for i in range(M):
    a, b = map(int, input().split())
    if a > b :
        B[a]+=1
    if b > a :
        B[b]+=1

count = 0
for i in range(N+1):
    if B[i] == 1 :
        count +=1

print(count)