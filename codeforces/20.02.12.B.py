from sys import stdin
import math
input=stdin.readline
for _ in range(int(input())):
    n,g,b=map(int,input().split())
    m = (n + 1)//2
    
    print(max(n,(math.ceil(m/g) - 1)*(g+b) + ((m - 1) % g) + 1))
