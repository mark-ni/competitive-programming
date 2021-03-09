from sys import stdin
input=stdin.readline
t=int(input())

def bc(x,k):
    l=[]
    m=1
    while m*k <= x:
        m *= k
    while m > 0:
        l.append(x//m)
        x %= m
        m //= k
    return l

for _ in range(t):
    n,k=map(int,input().split())
    a=sorted(list(map(int,input().split())),reverse=True)
    z=[0 for i in range(n)]
    z[0] = bc(a[0],k)
    l=len(z[0])
    for i in range(n):
        z[i] = bc(a[i],k)
        z[i] = [0]*(l - len(z[i])) + z[i]
    b=[0]*l
    for i in range(n):
        for j in range(l):
            b[j] += z[i][j]
    if max(b) > 1:
        print("NO")
    else:
        print("YES")
        
    
