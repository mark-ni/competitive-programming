from sys import stdin, stdout
#import math
from collections import deque

input = stdin.readline

asdf = [int(x) for x in input().split(' ')]
n = asdf[0]
skoolx = asdf[1]
skooly = asdf[2]
l = 0
r = 0
u = 0
d = 0

for i in range(n):
    li = [int(x) for x in input().split(' ')]
    if li[0] < skoolx: l += 1
    elif li[0] > skoolx: r += 1
    if li[1] < skooly: d += 1
    elif li[1] > skooly: u += 1
    
best = max([l,r,u,d])
if best == l: print(str(l) + "\n" + str(skoolx - 1) + ' ' + str(skooly))
elif best == r: print(str(r) + "\n" + str(skoolx + 1) + ' ' + str(skooly))
elif best == u: print(str(u) + "\n" + str(skoolx) + ' ' + str(skooly + 1))
else: print(str(d) + "\n" + str(skoolx) + ' ' + str(skooly - 1))