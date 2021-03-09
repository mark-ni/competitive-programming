from sys import stdin
input = stdin.readline

t=int(input())
for _ in range(t):
    n,s,k=map(int,input().split(' '))
    a = list(map(int,input().split(' ')))
    x = [True] * (n + 1)
    for i in a:
        x[i] = False
    lowestLower=(n+1)
    lowestHigher=(n+1)
    for i in range(s,max(s-k-1,0),-1):
        if x[i]:
            lowestLower = (s-i)
            break
    for i in range(s, min(s+k+1,n+1), 1):
        if x[i]:
            lowestHigher = (i-s)
            break
    print(min(lowestLower,lowestHigher))
