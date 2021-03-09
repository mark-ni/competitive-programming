from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for __ in range(t):
        n=int(input())
        print(*([1]*n))

def B():
    t=int(input())
    for __ in range(t):
        n=int(input())
        b=list(map(int,input().split()))
        d=dict()
        lefts=[set([])]*n
        rights=[set([])]*n
        for i in range(n):
            
            lefts[i].add(b[i])
            for j in lefts[i]:
                lefts[i].add(b[i] + 

4 7 7 8 10 15

1 2 5 9
9 2 5 1

def C():
    t=int(input())
    for __ in range(t):
        _=0

def D():
    t=int(input())
    for __ in range(t):
        _=0

A()
