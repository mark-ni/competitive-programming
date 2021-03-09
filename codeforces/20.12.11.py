from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n,x=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        if _ != t - 1: input()
        b.sort(reverse=True)
        a.sort()
        truth=True
        for i in range(n):
            if a[i]+b[i] > x:
                truth=False
                break
        if truth: print("Yes")
        else: print("No")

def B():
    t=int(input())
    for _ in range(t):
        a,b,c,d=map(int,input().split())
        print(max(a+b,c+d))
            
def D():
    n=int(input())
    a=sorted(list(map(int,input().split())))
    mod=998244353
    s=0
    ans=sum(a)
    for i in a[0:n]:
        ans -= 2*i
    ans %= mod
    num=1
    denom=1
    for i in range(n+1,2*n+1):
        num *= i
        num %= mod
    for i in range(1,n+1):
        denom *= i
        denom %= mod
    denom = pow(denom, mod - 2, mod)
    mult = (num * denom) % mod
    print((mult * ans) % mod)
            

D()
