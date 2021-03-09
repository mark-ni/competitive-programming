from heapq import heappop, heappush
from math import inf

n = int(input())
graph=[set() for i in range(n)]

for i in range(n):
    u,v,d=map(int,input().split())
    graph[u].add((v, d))
    graph[v].add((u, d))

def dj(head):
    vs=[-1 for i in range(n)]
    numVisited = 0
    dm=[inf for i in range(n)]
    pq=[]
    heappush(pq, (0, head))
    while len(pq) > 0 and numVisited < n:
        d,u=heappop(pq)
        if vs[u] == -1:
            vs[u]=numVisited
            numVisited += 1
            dm[u] = d
            for w,d0 in graph[u]:
                if vs[w] < 0:
                    heappush(pq,(w,d+d0))
    return dm

def prim(head):
    vs=[-1 for i in range(n)]
    numVisited = 0
    mst=[0]*(n - 1)
    pq=[]
    for v,d in graph[head]:
        heappush(pq,(head,v,d))
    vs[head]=0
    while len(pq) > 0 and numVisited < n - 1:
        u,w,d=heappop(pq)
        if vs[w] == -1:
            mst[numVisited]=((u,w))
            numVisited += 1
            vs[w] = numVisited
            for x,d0 in graph[w]:
                heappush(pq, (w,x,d0))
    return mst

            
    
    

