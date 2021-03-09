#from sys import stdin
#input=stdin.readline
import io,os
input=io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        p,c=[0]*n,[0]*n
        succ=True
        for i in range(n):
            p[i],c[i]=map(int,input().split())
        if p[0]<c[0]: succ=False
        else:
            for i in range(1,n):
                if c[i]-c[i-1]>p[i]-p[i-1] or c[i]<c[i-1] or p[i]<p[i-1]:
                    succ=False
                    break
        if succ: print("YES")
        else: print("NO")
    return

def B():
    t=int(input())
    for _ in range(t):
        n,x=map(int,input().split())
        a=list(map(int,input().split()))
        a.sort(reverse=True)
        tot,ppl=0,0
        for i in range(n):
            if a[i] + tot - x >= 0:
                ppl += 1
                tot += a[i] - x
            else: break
        print(ppl)
    return

def C():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a,b=[0]*n,[0]*n
        c=[0]*n
        for i in range(n):
            a[i],b[i]=map(int,input().split())
        c[0]=max(0,a[0]-b[n-1])
        s=c[0]
        for i in range(1,n):
            c[i]=max(0,a[i]-b[i-1])
            s+=c[i]
        m=a[0]-c[0]
        for i in range(1,n):
            if a[i]-c[i]<m:
                m=a[i]-c[i]
        print(s+m)
    return

def D():
    return

C()
