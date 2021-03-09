from sys import stdin
input = stdin.readline

n=int(input())
for i in range(n):
    a1,b1,c,r = map(int, input().split(' '))
    a = min(a1,b1)
    b = max(a1,b1)
    
    d = b - a
    e = min(c + r, b) - max(c - r, a)
    if e < 0:
        e = 0
    print(d - e)
    
    
