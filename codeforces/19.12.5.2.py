import sys
n = int(input())

def isBeautiful(seq, length):
    if set(seq) == set(range(1, length + 1)):
        return True
    else:
        return False

def getAns(k):
    li = [int(x) for x in input().split(' ')]
    liIndices = [0 for x in range(k + 1)]
    for i in range(k):
        liIndices[li[i]] = i

    currMax = liIndices[1]
    currMin = currMax
    currDiff = currMax - currMin
    for m in range(1, k + 1):
        if liIndices[m] > currMax:
            currMax = liIndices[m]
            currDiff = currMax - currMin
        elif liIndices[m] < currMin:
            currMin = liIndices[m]
            currDiff = currMax - currMin
        if currDiff < m:
            sys.stdout.write('1')
        else:
            sys.stdout.write('0')

for i in range(n):
    getAns(int(input()))
    print()
