from sys import stdin
input = stdin.readline
def f(x):
    if x == '0': return 1
    return -1

for _ in range(int(input())):
    n,x=map(int,input().split())
    s=[f(x) for x in input().rstrip()]
    for i in range(1,n):
        s[i]=s[i-1]+s[i]
    if s[n - 1] == 0:
        if x in s: print(-1)
        else: print(0)
    else:
        diff = abs(s[n-1])
        if (s[n-1] < 0):
            x *= -1
            for i in range(n):
                s[i]*=-1
        mod = x % diff
        tot = 0
        if (x==0):
            tot += 1
        for i in s:
            if i <= x and i % diff == mod:
                tot += 1
        print(tot)
