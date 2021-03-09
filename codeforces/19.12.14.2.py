#19.12.14.2.py
import sys
from collections import deque
#input = sys.stdin.readline

n = int(input())

def lastIndex(li, e):
    ind = -1
    for i in range(len(li)):
        if li[i] == e:
            ind = i
    return ind

def swap(i2, li):
    placehold = li[0]
    li[0] = li[i2]
    li[i2] = placehold
    
    return li

def optimize(string):
    x = sorted(string)
    newS = deque()
    for i in range(len(x)):
        if string[i] != x[i]:
            newS.extend(swap(lastIndex(string[i:],x[i]), string[i:]))
            break
        else:
            newS.append(x[i])
        
    return newS

for i in range(n):
    comps = [x for x in input().split(' ')]
    user = comps[0]
    opp = comps[1]
    if user < opp:
        print(user)
    else:
        string = ''.join(optimize(list(user)))
        if string < opp:
            print(string)
        else:
            print('---')