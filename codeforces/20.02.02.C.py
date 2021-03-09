from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    if k>=m:k=m-1
    a=list(map(int,input().split()))
    l=[max(a[i],a[i+n-m]) for i in range(m)]
    l2=[min(l[i:i+m-k]) for i in range(k+1)]
    print(max(l2))
