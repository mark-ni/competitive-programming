import math
t = int(input())
for _ in range(t):
    n,d=map(int,input().split(' '))
    if n >= d:
        print("YES")
    else:
        x=math.ceil(math.sqrt(d))
        if x-1 + math.ceil(d/x) <= n:
            print("YES")
        else:
            print("NO")
