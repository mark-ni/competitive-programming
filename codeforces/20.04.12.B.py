from sys import stdin
input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    b=[0]*n
    j=0
    while j < n:
        if j % 2 == 0: b[j] = a[j//2]
        else: b[j] = a[n - 1 - j//2]
        j+=1
    print(*b[::-1])    
