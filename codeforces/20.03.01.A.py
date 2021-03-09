from sys import stdin
from math import ceil
input=stdin.readline
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
badpts = 0
goodpts = 0
for i in range(n):
    if a[i] == 1 and b[i] == 0:
        goodpts += 1
    elif a[i] == 0 and b[i] == 1:
        badpts += 1
if goodpts == 0:
    print(-1)
else:
    badpts += 1
    print(ceil(badpts/goodpts))
    


#34 badpts, 3 good pts
        
    
