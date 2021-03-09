t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    print(min(m,a[0]+sum(a[1:])))
