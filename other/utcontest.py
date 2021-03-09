from sys import stdin
from collections import deque
input=stdin.readline
n,c,k=map(int,input().split())
s=list(map(int,input().split()))
prevInd = [-1]*n
prevIndEnd = [-1]*n
costs=[[] for i in range(n)]
values=[[] for i in range(n)]
for i in range(n):
    if prevInd[s[i]] == -1:
        prevInd[s[i]] = i
        prevIndEnd[s[i]] += 1
        values[s[i]].append(1)
    elif s[i] == s[i-1]:
        prevIndEnd += 1
        values[s[i]][-1] += 1
    
