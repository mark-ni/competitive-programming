import io, os
#input = io.StringIO(os.read(0, os.fstat(0).st_size).decode()).readline
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


#OBJECTIVE: Finding the size of every group within a disconnected graph

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
     
MOD = 10 ** 9 + 7
     
n, k = mi()
p, s = list(range(n + 1)), [1] * (n + 1)
     
def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]
     
def union(x, y):
    x, y = find(x), find(y)
    if x == y: return
    if s[x] < s[y]: x, y = y, x
    p[y] = x
    s[x] += s[y]
     
for _ in range(n - 1):
    u, v = mi()
    union(u, v)
     
grps = []
for u in range(1, n + 1):
    if p[u] == u:
        grps.append(s[u])
     
ans = (pow(n, k, MOD) - sum(pow(x, k, MOD) for x in grps)) % MOD
print(ans)
