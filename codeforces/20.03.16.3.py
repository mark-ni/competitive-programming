from heapq import heappop, heappush
from sys import stdout
from collections import deque, defaultdict

#from sys import stdin
#input=stdin.readline

import io,os
input=io.StringIO(os.read(0, os.fstat(0).st_size).decode()).readline

n,m=map(int,input().split())
d=[set() for i in range(n + 1)]
heap=[]
for i in range(m):
    u,v=map(int,input().split())
    d[u].add(v)
    d[v].add(u)
heap.append(1)
visited=[False for i in range(n + 1)]
while len(heap) > 0:
    sl=heappop(heap)
    if not visited[sl]:
        stdout.write(str(sl) + ' ')
        for e in d[sl]:
            heappush(heap, e)
            if e != sl:
                d[e].remove(sl)
        d[sl]=False
        visited[sl]=True

