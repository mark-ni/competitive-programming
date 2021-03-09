import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

def clearLi(l):
    for i in range(0, len(li)):
        l[i] = 0

for i in range(n):
    m = int(input())
    li = [int(x) - 1 for x in input().split(' ')]
    newli = [0] * len(li)
    d = deque()
    currSum = 0
    currIndex = 0
    for i in range(m):
        if newli[i] == 0:
            currSum = 1
            d.clear()
            d.append(i)
            
            currIndex = li[i]
            while not (currIndex == i):
                d.append(currIndex)
                currSum += 1
                currIndex = li[currIndex]
            
            for j in d:
                newli[j] = currSum
    print(*newli)