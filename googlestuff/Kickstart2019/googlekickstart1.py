import time

n = int(input())
def getAns(case):
    papers = int(input())
    cites = [int(x) for x in input().split(' ')]
    
    currentMax = 1
    string = str(currentMax)
    for i in range(1, len(cites)):
        currentCount = 0
        for j in range(0, i + 1):
            if cites[j] > currentMax:
                currentCount += 1
        if currentCount > currentMax:
            currentMax += 1
        string += ' ' + str(currentMax)
    
    print("Case #" + str(case) + ": " + string)

for i in range(n):
    getAns(i + 1)

#strin = "99999"
#for i in range(99998, -1, -1):
#    strin += ' ' + str(i)
#print(strin)
