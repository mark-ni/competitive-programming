import sys
#import math
from collections import deque
input = sys.stdin.readline

def findLongestSeq(l):
    runningneg = 0
    d = deque()

    running = 0
    m = 0
    for i in range(len(l)):
        if l[i] > 0:
            if runningneg > 0:
                if l[i] + l[i - 1] > 0 or l[i-1] + l[i-2]:
                    d.append(-1 * runningneg)
                else:
                    d.append(-2)
                runningneg = 0
            running += 1
        else:
            if running > 0:
                d.append(running)
                running = 0
            runningneg += 1
    if running > 0:
        d.append(running)
    elif runningneg > 0:
        d.append(-1 * runningneg)
    return d

n = int(input())
li0 = [int(x) for x in input().split(' ')]
newli = [0] * (n - 1)
foundpos = False

for i in range(n - 1):
    newli[i] = li0[i + 1] - li0[i]
    if newli[i] > 0:
        foundpos = True

if not foundpos:
    print(1)
else:
    y = findLongestSeq(newli)
    if y[0] < 0:
        y.popleft()
    if y[len(y) - 1] < 0:
        y.pop()

    if len(y) > 2:
        maxSum = 0
        currSum = 0
        for i in range(0, len(y) - 2, 2):
            if y[i + 1] == -1:
                currSum = y[i] + y[i + 2] + 1
            else:
                currSum = y[i] + 1
            if currSum > maxSum:
                maxSum = currSum
        print(maxSum)
    else:
        print(y[0] + 1)
        