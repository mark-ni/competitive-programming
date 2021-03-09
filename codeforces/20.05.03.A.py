from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
a=list(map(int,input().split()))
d=defaultdict()
x=[0]*(n+1)
tot=0
for i in range(n):
    x[i+1]=x[i]+a[i]
i=0
d[0]=0
for j in range(1,n + 1):
    if d.get(x[j], -1) != -1:
        i = d[x[j]] + 1
    tot += (j - i)
    d[x[j]] = j
print(tot)

