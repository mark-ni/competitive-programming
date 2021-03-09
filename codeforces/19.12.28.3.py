from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
s = list(map(int, input().split(' ')))

given = deque()
received = deque()

for i in range(n):
    if s[i] == 0:
        given.append(i + 1)
    else:
        received.append(s[i])

received = set(range(1, n+1)).difference(set(received))
given = set(given)

needBoth = list(received.intersection(given))
toreceive = list(received.difference(given))
togive = list(given.difference(received))

a = len(needBoth)
b = len(toreceive)

if a >= 2:
    s[needBoth[a-1] - 1] = needBoth[0]
    for i in range(0, a-1):
        s[needBoth[i] - 1] = needBoth[i+1]
    for i in range(b):
        s[togive[i] - 1] = toreceive[i]
else:
    if a == 1:
        e = needBoth[0]
        s[e - 1] = toreceive[0]
        for i in range(b - 1):
            s[togive[i] - 1] = toreceive[i+1]
        s[togive[b-1] - 1] = e
    else:
        for i in range(b):
            s[togive[i] - 1] = toreceive[i]

print(*s)
    
        
