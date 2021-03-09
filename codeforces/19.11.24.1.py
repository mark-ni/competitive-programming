n = int(input())
import math

def getAns(k):
    mins = []
    maxs = []
    currentLineList = []
    for i in range(k):
        currentLineList = [int(x) for x in input().split(' ')]
        mins.append(currentLineList[0])
        maxs.append(currentLineList[1])
    diff = max(mins) - min(maxs)
    if diff < 0:
        print(0)
    else:
        print(diff)
        
for i in range(n):
    getAns(int(input()))