from sys import stdin
from collections import deque
from math import sqrt, floor
input=stdin.readline

def getFactors(k):
    d=deque()
    for i in range(1, floor(sqrt(k))+1):
        if k % i == 0:
            d.append(i)
    return list(d)

def getFits(factorsList, k, length, width):
    tot=0
    for i in factorsList:
        j=k//i
        added=0
        if length >= i and width >= j:
            tot += (length + 1 - i) * (width + 1 - j)
            added+=1
        if length >= j and width >= i:
            tot += (width + 1 - i) * (length + 1 - j)
            added+=1
        if i == j and added==2:
            tot -= (width + 1 - i) * (length + 1 - j)
        #print("TOT FOR " +str(i) + ": " + str(tot))
    return tot

n,m,k=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

factors=getFactors(k)
#print(str(factors))

rowWidths=deque()
antiRowWidths=deque()
currNum=1
currCount=0
for i in range(m):
    if b[i] != currNum:
        if currCount > 0:
            if currNum == 1: rowWidths.append(currCount)
            else: antiRowWidths.append(currCount)
        currNum = b[i]
        currCount = 0
    currCount += 1
if b[m - 1] == 1: rowWidths.append(currCount)
else: antiRowWidths.append(currCount)

#print(str(rowWidths))
#print(str(antiRowWidths))

rectLengths=deque()
rectWidths=deque()
currNum=1
currCount=0
for i in range(n):
    if a[i] != currNum:
        if currCount > 0:
            if currNum == 1:
                for j in rowWidths:
                    rectWidths.append(j)
                    rectLengths.append(currCount)
            else:
                for j in antiRowWidths:
                    rectWidths.append(j)
                    rectLengths.append(currCount)
        currCount = 0
        currNum = a[i]
    currCount += 1
if currNum == 0:
    for j in antiRowWidths:
        rectWidths.append(j)
        rectLengths.append(currCount)
else:
    for j in rowWidths:
        rectWidths.append(j)
        rectLengths.append(currCount)
tot=0
for i in range(len(rectLengths)):
    #print((rectLengths[i],rectWidths[i]))
    tot += getFits(factors,k,rectLengths[i],rectWidths[i])
print(tot)
