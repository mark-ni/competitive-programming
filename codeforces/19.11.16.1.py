'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import math

def getAns(li1, li2):
    li3 = []
    diff = 0
    theDiff = 0
    firstOccurrence = True
    onARoll = False

    for i in range(len(li1)):
        diff = li2[i] - li1[i]
        if diff != 0:
            if diff < 0:
                return "NO"
            if firstOccurrence:
                firstOccurrence = False
                theDiff = diff
            elif not firstOccurrence and not onARoll:
                return "NO"
            elif theDiff != diff:
                return "NO"
            onARoll = True
        else:
            onARoll = False
    return "YES"
n = int(input())

for i in range(n):
    input()
    #firstLi = [int(x) for x in input().split(' ')]
    #secondLi = [int(y) for y in input().split(' ')]
    print(getAns([int(x) for x in input().split(' ')], [int(y) for y in input().split(' ')]))
    
    