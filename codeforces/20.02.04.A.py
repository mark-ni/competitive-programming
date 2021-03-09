from sys import stdin
input = stdin.readline
t= int(input())

def getAns(n, l):
    if (n % 2 == 1):
        for i in l:
            if i % 2 == 1:
                return True
    else:
        foundEven = False
        foundOdd = False
        for i in l:
            if i % 2 == 0:
                foundEven = True
            else:
                foundOdd = True
        return (foundEven and foundOdd)

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if getAns(n,l):
        print("YES")
    else:
        print("NO")
        
