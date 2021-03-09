from sys import stdin
input=stdin.readline

n = int(input())
q = list(map(int,input().split()))
peaksSums = [0]*n
currBestIndex = 0
currHighestSum = -1
for i in range(0, n):
    m = q[i]
    tot = 0
    for j in range(i - 1, -1, -1):
        if q[j] > m:
            tot += m
        else:
            tot += q[j]
            m = q[j]
    m = q[i]
    for j in range(i + 1, n):
        if q[j] > m:
            tot += m
        else:
            tot += q[j]
            m = q[j]
    tot += q[i]
    if tot > currHighestSum:
        currBestIndex = i
        currHighestSum = sum(m)
i=currBestIndex
for j in range(i - 1, -1, -1):
    if q[i] > q[i + 1]:
        q[i] = q[i + 1]
    for j in ran
print(*q)
