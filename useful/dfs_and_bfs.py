from collections import deque
from heapq import heappop, heappush

n=int(input())
graph=[deque() for i in range(n)]
for i in range(n):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited=[0 for i in range(n)]
nodeVisited = 1

def dfs(node):
    visited[node] = nodeVisited
    nodeVisited += 1
    for i in g[node]:
        if visited[node] == 0:
            dfs(node)

def bfs(head):
    visited = nodeVisited
    queue = deque([head])
    while len(queue) > 0:
        curr = queue.pop()
        for adj in graph[curr]:
            if visited[adj] == 0:
                nodeVisited += 1
                visited[adj] = nodeVisited
                queue.appendleft(adj)

print(str(visited))
    
        
