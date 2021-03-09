from sys import stdin,stdout
input=stdin.readline

n=int(input())
counts=[0]*(n+1)
rawData=[set() for i in range(n)]
placeIndices=[set() for i in range(n+1)]
for i in range(n-2):
    rawData[i]=set(map(int,input().split()))
    for j in rawData[i]:
        placeIndices[j].add(i)
currAns=[]
oneIndex = 0
for i in range(1,n+1):
    if len(placeIndices[i])==1:
        oneIndex = i
        rawData[i].remove(one)
        break
stdout.write(str(one) + ' ')
for i in range(n - 2):
    rawData[oneIndex].remove(oneIndex)
    for j in rawData[oneIndex]:
        if len(placeIndices[j]) == 3:
            placeIndices[j].remove(oneIndex)
        

for i in rawData[one]:
    if len(placeIndices[i]) == 2:
        placeIndices[i].remove(one)
        nextOne=placeIndices[i].pop()
        stdout.write(str(nextOne) + ' ')
    else:
        placeIndices[i].remove(one)
one=nextOne
rawData[i].remove(one)
for i in rawData[
