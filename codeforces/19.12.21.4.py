from sys import stdin
from collections import deque

n = int(input())

def getAns(n, l):
    tot = 0
    c = 1
    d = deque()
    
    while c < n:
        if l[c] % 2 == l[c - 1] % 2:
            tot += (l[c] + l[c-1])//2
            l[c] = 0
            l[c - 1] = 0
            c += 2
        else:
            c += 1
    k =0 
    for i in l:
        if i % 2 == 1:
            k += 1
    tot += (sum(l) - k)//2
    return tot

print(getAns(n, list(map(int, input().split(' ')))))
