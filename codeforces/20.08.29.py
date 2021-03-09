from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=input()
        print(s[n-1]*n)

from collections import deque

def D():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))

        dfind=[[0 for i in range(n)] for j in range(n)]
        afind=[[0 for i in range(n)] for j in range(n)]

        for secondInd in range(1, n-2):
            for thirdInd in range(n-2, secondInd, -1):
                bonus=int(a[thirdInd+1]==a[secondInd])
                dfind[secondInd][thirdInd]=dfind[secondInd][thirdInd+1]+bonus
        for thirdInd in range(2, n-1):
            for secondInd in range(1, thirdInd):
                bonus=int(a[secondInd-1]==a[thirdInd])
                afind[secondInd][thirdInd]=afind[secondInd-1][thirdInd]+bonus

        tot=0
        for secondInd in range(1, n-2):
            for thirdInd in range(secondInd, n-1):
                tot += afind[secondInd][thirdInd] * dfind[secondInd][thirdInd]
        print(tot)
        
D()    

    
    

    
    
    
    
    
    
