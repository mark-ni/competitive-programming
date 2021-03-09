from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for __ in range(t):
        n,m=map(int,input().split())
        a=list(map(int,input().split()))
        if sum(a) == m: print("YES")
        else: print("NO")

def B():
    t=int(input())
    for __ in range(t):
        n=int(input())
        x=[[0 for j in range(n)] for i in range(n)]
        for i in range(n//2):
            x[i][i]=1
            x[i][n-1-i]=1
            x[n-1-i][i]=1
            x[n-1-i][n-1-i]=1
        if n % 2 == 1:
            x[n//2-1][n//2] = 1
            x[n//2+1][n//2] = 1
            x[n//2][n//2+1] = 1
            x[n//2][n//2-1] = 1
        for i in range(n):
            print(*x[i])

def C():
    n,x,pos=map(int,input().split())
    numLess=x-1
    numMore=n-x
    nume=1
    denom=1
    left=0
    right=n
    mod = pow(10,9) + 7
    
    while left < right:
        mid = (left + right) // 2
        if mid < pos:
            nume *= numLess
            denom *= (numLess + numMore)
            numLess -= 1
            left = mid + 1
        elif mid > pos:
            nume *= numMore
            denom *= (numLess + numMore)
            numMore -= 1
            right = mid
        else:
            left = mid + 1
        nume %= mod
        denom %= mod
    fact=1
    for i in range(2,n):
        fact *= i
        fact %= mod
    fract = (nume * (pow(denom, mod-2, mod))) % mod
    print((fract * fact) % mod)
    

def D():
    n=int(input())
    p=list(map(int,input().split()))
    a=list(map(int,input().split()))
    

D()
