import math, random
from sys import stdin, stdout
input = stdin.readline

t = int(input())
s = ""

def toTakeAway(q):
    return (q * (q + 1))//2

def f(n,m,l=True):
    p = n - m
    #there are p % m of the higher and m - p%m of the lower
    numGaps = m + 1
    numHigher = p % numGaps
    numLower = numGaps - numHigher
    higher = math.ceil(p / numGaps)
    lower = p//numGaps
    totalTaken = toTakeAway(higher) * numHigher + toTakeAway(lower) * numLower

    if l:
        stdout.write(str(toTakeAway(n) - totalTaken) + "\n")
    else:
        s = str(toTakeAway(n) - totalTaken) + "\n"

def g():
    for i in range(100000):
        f(1000000000, random.randrange(1,1000000000),False)
    

for _ in range(t):
    n,m=map(int,input().split())
    f(n,m)

    
    
