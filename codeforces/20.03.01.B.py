from sys import stdin
from collections import defaultdict
input=stdin.readline
n=int(input())
b=list(map(int,input().split()))
d=defaultdict()
for i in range(n):
    key=b[i]-i-1
    d[key]=d.get(key,0)+b[i]
print(max(list(d.values())))
    

