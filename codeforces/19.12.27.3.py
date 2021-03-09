from sys import stdin
from collections import deque
input = stdin.readline

q = int(input())
for _ in range(q):
    n,m=map(int,input().split(' '))
    a=deque(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))

    s = set([])
    moves = 0
    actual = 0
    
    for i in range(m):
        if b[i] in s:
            moves += 1
            s.remove(b[i])
            actual -= 1
        else:
            k = a.index(b[i])
            moves+=2*(k + actual) + 1
            for i in range(k):
                s.add(a.popleft())
                actual += 1
            a.popleft()
    print(moves)
            
