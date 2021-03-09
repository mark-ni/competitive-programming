from collections import deque
n = int(input())

def getAns(k):
    d = deque()
    found0 = 0
    foundEven = False

    for i in k:
        if i == "0":
            found0 += 1
        else:
            d.append(int(i))
    if found0 > 1:
        foundEven = True
    else:
        for i in d:
            if i % 2 == 0:
                foundEven = True
                break
    if foundEven and found0 > 0 and sum(d) % 3 == 0:
        print("red")
    else:
        print("cyan")


for i in range(n):
    getAns(list(input()))
