from sys import stdin
input=stdin.readline

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    p=sorted(list(map(int,input().split())))
    foundSwap = True
    while foundSwap:
        foundSwap = False
        for i in p:
            if a[i - 1] > a[i]:
                foundSwap = True
                temp = a[i]
                a[i] = a[i - 1]
                a[i - 1] = temp
    if a == sorted(a):
        print("YES")
    else:
        print("NO")
