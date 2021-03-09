from sys import stdin,stdout
input=stdin.readline

def A():
    for _ in range(int(input())):
        n,m=map(int,input().split())
        print('W' + 'B' * (m - 1))
        for i in range(1,n): print('B' * m)

def B():
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        foundNeg=False
        foundPos=False
        succ=True
        for i in range(n):
            if a[i] > b[i]:
                if not foundNeg:
                    succ=False
                    break
            elif a[i] < b[i]:
                if not foundPos:
                    succ=False
                    break
            if a[i] > 0: foundPos=True
            elif a[i] < 0: foundNeg=True
        if succ: print("YES")
        else: print("NO")
    return

def C():
    from collections import defaultdict
    n=int(input())
    a=list(map(int,input().split()))
    d=defaultdict()
    d[0]=-1
    b=[a[0]]*n
    for i in range(1,n):
        b[i]=b[i-1]+a[i]
    front=-1
    tot=0
    for j in range(n):
        x=d.get(b[j],-2)
        if x >= front:
            front = x + 1
        tot += (j - front)
        d[b[j]]=j
    print(tot)


def D():
    n,k=map(int,input().split())
    d=[bool(ord(x)-76) for x in input().rstrip()]
    mids=[-1]*(n+1)
    for mid in range(n+1):
        e=d.copy()
        y=0
        for i in range(mid):
            if e[i]:
                e[i] = not e[i]
                e[i+1] = not e[i+1]
        for i in range(mid, n):
            if not e[i]
        
        
    return

C()



