import math

n = int(input())

for i in range(n):
    input()
    li = input().split(' ')
    newLi = []
    
    print(getAns([int(x) for x in input().split(' ')]))

def getAns(li):
    li = li.sort()
