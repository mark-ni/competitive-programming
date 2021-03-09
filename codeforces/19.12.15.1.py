from sys import stdin, stdout
#import math
#from collections import deque

input = stdin.readline
tot = 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if e > f:
    x = min(a, d)
    d -= x
    tot += x * e
    y = min([b,c,d])
    tot += y * f
else:
    x = min([b,c,d])
    d -= x
    tot += x * f
    y = min(a, d)
    tot += y * e
print(tot)