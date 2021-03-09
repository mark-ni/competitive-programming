from itertools import permutations 
import math

def solve(permut,numFactors):
    currentMin = 10**9
    goodProd1 = 0
    goodProd2 = 0
    for i in range(numFactors+1):
        prod1 = 1
        prod2 = 1
        for j in range(0,i):
            prod1 *= permut[j]
        for j in range(i,numFactors):
            prod2 *= permut[j]
        if max(prod1,prod2)<currentMin:
            currentMin = max(prod1, prod2)
            goodProd1 = prod1
            goodProd2 = prod2
    return currentMin,goodProd1,goodProd2

def getAns(n):
    factorsRaw = [0]*(int(math.sqrt(n)+10))
    while n % 2 == 0:
        factorsRaw[2] += 1
        n//=2
    for i in range(3, int(math.sqrt(n))+3,2):
        while n%i==0:
            factorsRaw[i] += 1
            n//=i
    #print(str(factorsRaw))
    if n > 2:
        print('1 ' + str(n))
        #print("lmao!")
    else:
        factors = []
        for i in range(len(factorsRaw)):
            if factorsRaw[i] > 0:
                factors.append(i**factorsRaw[i])
        permuts = list(permutations(factors))
        currentMin = 10**9
        s = len(factors)
        currentProd1 = 0
        currentProd2 = 0

        for i in permuts:
            x,y,z = solve(i,s)
            if x < currentMin:
                currentMin = x
                currentProd1 = y
                currentProd2 = z
                
        print(*list(sorted([y,z])))

getAns(int(input()))
    
            
    
