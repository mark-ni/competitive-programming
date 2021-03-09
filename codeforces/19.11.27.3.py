def computeGCD(x, y):
    if (y == 0):
        return x
    else:
        return computeGCD(y, x % y)

n = int(input())
import math

def getAns(arr):
    r = arr[0]
    b = arr[1]
    k = arr[2]
    
    if (k <= 1):
        print("REBEL")
        return
    
    if (r > b):
        bigger = r
        smaller = b
    else:
        bigger = b
        smaller = r
    
    theGCD = computeGCD(bigger, smaller)
    bigger//=theGCD
    smaller//=theGCD
    cap = math.ceil((bigger - 1)/smaller)

    if cap < k:
        print("OBEY")
    else:
        print("REBEL")
    
    
for i in range(n):
    getAns([int(x) for x in input().split(' ')])
    
    