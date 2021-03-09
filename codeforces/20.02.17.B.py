import math
t = int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if x in a:
        print(1)
    elif max(a) >= x/2:
        print(2)
    else:
        print(math.ceil(x/max(a)))
        
