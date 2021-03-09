n = int(input())
    
for i in range(n):
    length = int(input())//2 + 1
    li = [int(x) for x in input().split(' ')][0:length]
    
    currentNum = li[-1]
    for e in range(len(li) - 2, -1, -1):
        if li[e] != currentNum:
            li = li[0:e + 1]
            length = len(li)
            break

    currentNum = li[0]
    currentCount = 1
    l = []
    for e in range(1, length):
        if li[e] == currentNum:
            currentCount += 1
        else:
            l.append(currentCount)
            currentCount = 1
            currentNum = li[e]
    l.append(currentCount)
    
    gsb = [0, 0, 0]
    gsb[0] = l[0]
    for i in range(1, len(l)):
        gsb[1] += l[i]
        if gsb[1] > gsb[0]:
            gsb[2] = sum(l[i+1:])
            break
    if gsb[0] < gsb[1] and gsb[0] < gsb[2]:
        print(*gsb)
    else:
        print("0 0 0")
