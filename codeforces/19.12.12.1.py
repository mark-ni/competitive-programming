import sys
#import math
#from collections import deque

input = sys.stdin.readline

def getAns(k):
    s = min(k)
    l = max(k)
    if s < l:
        s += 1
    if l > s:
        l -= 1
    print(2 * l - 2 * s)

n = int(input())

for i in range(n):
    getAns([int(x) for x in input().split(' ')])