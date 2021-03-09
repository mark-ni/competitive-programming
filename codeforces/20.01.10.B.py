from sys import stdin
input = stdin.readline

def getAns(n,a):
    b = [a[0]]+[0]*(n-1)
    if b[0]<0: b[0]=0
    for i in range(1,n):
        b[i] = a[i]+b[i-1]
        if b[i] < 0:
            b[i] = 0
    if sum(a)>max(b) or (b.index(max(b)) == n-1 and 0 not in b):
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split(' ')))
    getAns(n,a)
