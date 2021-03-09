from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
graph=[set() for i in range(n+1)]
visited2=[False]*(n+2)
for i in range(n - 1):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)
k=0
for i in range(n + 1):
    if len(graph[i]) == 1:
        k=i
        break
m=[1,n-1]
def dfs(node, depth):
    nodes=deque([node])
    depths=deque([depth])
    while len(nodes) > 0:
        node=nodes.popleft()
        depth=depths.popleft()
        visited2[node] = True
        went=False
        for i in graph[node]:
            if not visited2[i]:
                nodes.appendleft(i)
                depths.appendleft(depth+1)
                went=True
        if not went:
            if depth % 2 == 1 and depth != 1:
                m[0] = 3
dfs(k,0)
oneBranches=[0]*(n+1)
for i in range(1,n+1):
    if len(graph[i]) == 1:
        oneBranches[graph[i].pop()] += 1
for i in range(n+1):
    if oneBranches[i] > 1:
        m[1] -= oneBranches[i] - 1
print(*m)

#if there is odd path length, min is 3 else 1
#max length: each odd unvisited path gives n, while each even unvisited path gives n - 1
