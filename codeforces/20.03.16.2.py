from collections import deque
n,k=map(int,input().split())
sets=[set() for i in range(n + 1)]

def dfs(node):
    tot = 1
    for i in sets[node]:
        sets[i].remove(node)
        tot += dfs(i)
    sets[node].clear()
    return tot

emptys=set()
for i in range(n - 1):
    u,v,x=map(int,input().split())
    if x == 0:
        sets[v].add(u)
        sets[u].add(v)
    else:
        if len(sets[u]) == 0:
            emptys.add(u)
        if len(sets[v]) == 0:
            emptys.add(v)
tot = 0
for i in emptys:
    if len(sets[i]) == 0:
        tot += 1

mod = pow(10,9)+7
for i in range(len(sets)):
    if len(sets[i]) > 0:
        tot += pow(dfs(i),k,mod)
        tot %= mod

print((pow(n,k,mod) - tot) % mod)
