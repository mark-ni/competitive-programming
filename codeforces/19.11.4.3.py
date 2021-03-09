
li = []
list1 = [int(x) for x in input().split(' ')]
l = list1[0]
p = list1[1]
j = list1[2] - 1
platLengths = [int(x) for x in input().split(' ')]
if j * (p + 1) + sum(platLengths) >= l:
    print("YES")
    
    currentPlat = 1
    if (j == 0):
        for i in range(currentPlat - 1, p):
            li += [currentPlat] * platLengths[i]
            currentPlat += 1
    else:
        jumpSpaces = l - sum(platLengths)
        numFullJumps = jumpSpaces // j #4
        leftOverJump = jumpSpaces % j #2
        
        numJumps = numFullJumps
        if leftOverJump > 0:
            numJumps += 1

        if numFullJumps >= p:
            for i in range(numFullJumps - (numFullJumps - p)):
                li += [0] * j
                li += [currentPlat] * platLengths[currentPlat - 1] #0, 0 -- 1, 1, -- 2,2
                currentPlat += 1
            li += [0] * (l - len(li))
        else:
            for i in range(numFullJumps):
                li += [0] * j
                li += [currentPlat] * platLengths[currentPlat - 1]
                currentPlat += 1
            li += [0] * leftOverJump
            for i in range(currentPlat - 1, p):
                li += [currentPlat] * platLengths[currentPlat - 1]
                currentPlat += 1
    print(*li)
    
else:
    print("NO")


