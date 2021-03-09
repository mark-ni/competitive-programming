from sys import stdin
from math import floor, log
from collections import deque
input=stdin.readline

def nToB(n,b):
    currPow = log(n,b)
    if (b ** round(currPow) == n):
        currPow = round(currPow)
    else:
        currPow = floor(currPow)
    d=deque()
    while (currPow > -1):
        mod=b**currPow
        d.appendleft(n // mod)
        n %= mod
        currPow -= 1
    return d

def getAns(n,k,a):
    l=[0]*(floor(log(a[0],k)) + 2)
    for i in a:
        if i == 0: break
        d=nToB(i,k)
        for j in range(len(d)):
            l[j] += d[j]
            if l[j] > 1:
                print("NO")
                return
    print("YES")
    

T=int(input())
for _ in range(T):
    n,k=map(int,input().split())
    a=sorted(list(map(int,input().split())), reverse=True)
    if a[0] == 0:
        print("YES")
    else:
        getAns(n,k,a)
                
