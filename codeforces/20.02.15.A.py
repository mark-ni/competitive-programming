from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    x,y,a,b=map(int,input().split())
    if (y - x) % (a + b) == 0:
        print((y - x)//(a + b))
    else:
        print(-1)
