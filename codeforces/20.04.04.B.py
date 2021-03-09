from sys import stdin
input=stdin.readline

def getSub(a,n):
    visited=[False] * (n + 1)
    currMax=0
    tru = [False]*(n)
    for i in range(n - 1):
        if visited[a[i]]: break
        visited[a[i]] = True
        if a[i] > currMax: currMax = a[i]
        if i + 1 == currMax: tru[i+1]=True
    return tru

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=getSub(a,n)
    c=getSub(a[::-1],n)
    good=set()
    for i in range(n):
        if b[i] and c[n - i]: good.add((i,n-i))
    print(len(good))
    for l1,l2 in good: print(l1,l2)

                
        
        
        
    
