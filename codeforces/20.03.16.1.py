from collections import defaultdict
from sys import stdin
input=stdin.readline
def getAns(d):
    for i in d.keys():
        if d[i] == 2:
            print("NO")
            return
    print("YES")
d=defaultdict()
n=int(input())
for i in range(n - 1):
    u,v=map(int,input().split())
    d[u]=d.get(u,0)+1
    d[v]=d.get(v,0)+1
getAns(d)
    
