from collections import deque
n,m,k=map(int,input().split())
p=deque(int(x) - 1 for x in input().split())
numRemoved = 0
ops = 0
while len(p) > 0:
    currRemoved = 1
    front = p.popleft()
    currPage = (front - numRemoved)//k
    #print(str(ops) + ": " + str(front))
    while (len(p) > 0 and (p[0] - numRemoved)//k == currPage):
        currRemoved += 1
        p.popleft()
    ops += 1
    numRemoved += currRemoved
print(ops)
    
