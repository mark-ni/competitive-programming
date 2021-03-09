n = int(input())
for i in range(n):
    n,k = map(int, input().split(' '))
    d=n%k
    print(n) if d<=k//2 else print(n-(d-k//2))
