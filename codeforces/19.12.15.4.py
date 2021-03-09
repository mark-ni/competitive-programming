from sys import stdin, stdout
#import math
from collections import deque

input = stdin.readline

asdf = [int(x) for x in input().split(' ')]
n = asdf[0]
m = asdf[1]
k = asdf[2]
for i in range(n):
    #CASTLES
    castle = [int(x) for x in input().split(' ')]
    req = castle[0]
    stationed = castle[1]
    importance = castle[2]
for i in range(m):
    #PORTALS
    portal = [int(x) for x in input().split(' ')]