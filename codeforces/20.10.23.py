from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        c=list(map(int,input().split()))
        p=[0]*n
        p[0] = a[0]
        for i in range(1, n-1):
            if a[i] != p[i - 1]: p[i] = a[i]
            else: p[i] = b[i]
        if a[n-1] != p[0] and a[n-1] != p[n-2]: p[n-1] = a[n-1]
        elif b[n-1] != p[0] and b[n-1] != p[n-2]: p[n-1] = b[n-1]
        else: p[n-1] = c[n-1]
        print(*p)
        

def B():
    from math import ceil
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        a=len(sorted(list(set(a))))
        if a <= k:
            print(1)
        else:
            a -= k
            if k == 1: print(-1)
            else: print(1 + ceil(a/(k - 1)))

def C():
    t=int(input())
    for _ in range(t):
        n,l=map(int,input().split())
        a=[0] + list(map(int,input().split())) + [l]
        t1=[0]*(n+2)
        v1=[1]*(n+2)
        t2=[0]*(n+2)
        v2=[1]*(n+2)
        for i in range(1,n+2):
            t1[i] = (a[i] - a[i - 1])/v1[i - 1] + t1[i - 1]
            v1[i] = v1[i - 1] + 1
        for i in range(n, -1, -1):
            t2[i] = (a[i + 1] - a[i])/v2[i + 1] + t2[i + 1]
            v2[i] = v2[i + 1] + 1
        A,B=0,0
        for i in range(n+1):
            if t1[i] == t2[i]:
                A,B=i,i
                print(t1[i])
                break
            if not (t1[i+1] < t2[i+1] or t1[i] > t2[i]):
                A,B=i,i+1
                break
        if A == B: continue
        t = (v1[A]*t1[A] + v2[B]*t2[B] + a[B] - a[A]) / (v1[A] + v2[B])
        print(t)

def D():
    n,m=map(int,input().split())
    a,b,c,d=[0]*n,[0]*n,[0]*m,[0]*m
    xofy=[0]*1000001
    corners=
    for i in range(n):
        a[i],b[i]=map(int,input().split())
    for i in range(n):
        c[i],d[i]=map(int,input().split())
        xofy[d[i]] = max(xofy[d[i]],c[i])
    for i in range(1,1000001):
        xofy[i] = max(xofy[i],xofy[i-1])
    dy=[0]*1000001
    s=1000000 - max(b)
    for i in range(1,s):
        
        

def E():
    t=int(input())
    for _ in range(t):
        __=0

def F():
    t=int(input())
    for _ in range(t):
        __=0

D()
