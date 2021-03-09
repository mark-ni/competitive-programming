from sys import stdin
input = stdin.readline

def getAns(n,m):
    c = sorted([list(map(int,input().split())) for i in range(n)])
    l,h,t = m,m,0
    for i in range(n):
        if c[i][0] - t + h < c[i][1] or l - (c[i][0] - t) > c[i][2]: return "NO"
        l,h,t = max(c[i][1], l - (c[i][0] - t)), min(c[i][2], h + (c[i][0] - t)), c[i][0]
    return "YES"

for _ in range(int(input())):
    n,m=map(int,input().split())
    print(getAns(n,m))
    
