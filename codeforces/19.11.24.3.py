def craftIdeal(length, zeroes):
    asdf = []
    x = 0
    for i in range(zeroes - 1):
        asdf.append(True)
        asdf.append(False)
        x += 2
    for j in range(x, x + (length - x)//2):
        asdf.append(True)
    for k in range(x + (length - x)//2, length):
        asdf.append(False)
    return asdf

def getAns(string, l, m):
    real = []
    for char in string:
        if char == ")":
            real.append(False)
        else:
            real.append(True)
    endgoal = craftIdeal(l, m)
    operations = []
    temp = []
    
    for i in range(l):
        target = endgoal[i]
        if real[i] != target:
            nextDiffIndex = i + 1
            while real[nextDiffIndex] != target:
                nextDiffIndex += 1
                
            temp = real[i:nextDiffIndex + 1]
            for j in range(i, nextDiffIndex + 1):
                real[j] = temp[nextDiffIndex - j]
                
            operations.append(str(i + 1) + " " + str(nextDiffIndex + 1))
    print(len(operations))
    for e in operations:
        print(e)
    return
    
n = int(input())
for i in range(n):
    k = [int(x) for x in input().split(' ')]
    getAns(input(), k[0], k[1])
