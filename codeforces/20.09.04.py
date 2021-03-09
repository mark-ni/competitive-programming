from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        if len(set(a)) == 1:
            print(n)
        else:
            print(1)

def B():
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        d=max(a)
        for i in range(n): a[i]=d-a[i]
        if k % 2 == 1: print(*a)
        d=max(a)
        for i in range(n): a[i]=d-a[i]
        if k % 2 == 0: print(*a)

def C():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        ops=0
        for i in range(n-1,0,-1):
            if a[i] < a[i - 1]:
                ops += a[i - 1] - a[i]
        print(ops)

def D():
    from collections import deque
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=[bool(ord(x)-ord('L')) for x in input().rstrip()]
        curr=s[0]
        d=deque()
        for i in range(1,n):
            if s[i] != curr:
                curr=s[i]
                d.append(i)
        #[4,6,7,10], n=12
        tot=0
        for i in range(1, len(d)):
            tot += (d[i] - d[i-1])//3
        if len(d) == 0:
            tot=(n+2)//3
        elif s[-1]==s[0]:
            tot += (d[0]+(n-d[-1]))//3
        else:
            tot += d[0]//3
            tot += (n-d[-1])//3
        print(tot)
D()
