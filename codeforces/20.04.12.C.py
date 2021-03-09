from sys import stdin
input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*n
    for i in range(1,n):
        if a[i] < a[i - 1]:
            b[i] = len(bin(a[i - 1] - a[i]))-2
            a[i] = a[i - 1]
    print(max(b))
        
