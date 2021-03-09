from sys import stdin,stdout
input=stdin.readline
n = int(input())
a = list(map(int,input().split()))
t = list(map(int,input().split()))
l = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    l[i][0]=a[i]
    l[i][1]=t[i]
l.sort()
l0 = [0]*n
l1 = [0]*n
for i in range(n):
    l0[i]=l[i][0]
    l1[i]=l[i][1]
time = 0
prevInd = 1
currInd = 1
currNum = l0[0]
while prevInd < n:
    #check for many of the same number in a row
    currInd = prevInd
    while currInd < n and l0[currInd]==currNum:
        currInd += 1
    #handle having many of the same number in a row
    #by increasing all but most expensive by 1
    if currInd > prevInd:
        mostTime = l1[prevInd]
        mostTimeIndex = prevInd
        for i in range(prevInd - 1, currInd):
            l0[i] += 1
            time += l1[i]
            if l1[i] > mostTime:
                mostTime = l1[i]
                mostTimeIndex = i
        time -= l1[mostTimeIndex]
        l0[mostTimeIndex] -= 1
        #Swap positions of mostTimeIndex
        l0[prevInd - 1],l0[mostTimeIndex]=l0[mostTimeIndex],l0[prevInd-1]
        l1[prevInd - 1],l1[mostTimeIndex]=l1[mostTimeIndex],l1[prevInd-1]
    currNum = l0[prevInd]
    prevInd+=1

#for i in range(n):
#    stdout.write(str(l[i][0]))
#    stdout.write(' ')
#print()
stdout.write(str(time))
    
