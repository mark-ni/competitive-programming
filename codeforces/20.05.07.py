t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        a[i] = (i + a[i]) % n
    if len(set(a)) == n: print("YES")
    else: print("NO")
