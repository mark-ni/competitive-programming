from sys import stdin
input=stdin.readline
n=int(input())
b=list(map(int,input().split()))
a=[0]*n
x=[0]*n
a[0]=b[0]
for i in range(1,n):
    x[i]=max(x[i - 1],a[i - 1])
    a[i]=b[i] + x[i]
print(*a)
    
