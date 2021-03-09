from sys import stdin
from collections import defaultdict
input = stdin.readline
t = int(input())

def getAns(n,s):
    d = defaultdict()
    currPos = 0
    currMin = n + 1
    currMins = -1
    d[0] = 0
    for i in range(n):
        if s[i] == 'L': currPos -= n
        elif s[i] == 'R': currPos += n
        elif s[i] == 'U': currPos += 1
        else: currPos -= 1
        if (d.get(currPos)) != None:
            if i + 1 - d[currPos] < currMin:
                currMin = i + 1 - (d[currPos])
                currMins = [d[currPos], i + 1]
        d[currPos] = i + 1
    if currMins == -1:
        print(-1)
        return
    else:
        currMins[0] += 1
        print(*currMins)
        return
        
    
for _ in range(t):
    n = int(input())
    s = list(input())
    getAns(n,s)
            
    
