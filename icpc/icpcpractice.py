from sys import stdin
input=stdin.readline

def D():
    n,m=map(int,input().split())
    connects=[set() for i in range(n)]
    for i in range(m):
        u,v=map(int,input().split())
        u,v=u-1,v-1
        connects[u].add(v)
        connects[v].add(u)
    g=[set() for i in range(n)]
    for i in range(n):
        for j in connects[i]:
            g[i].update(connects[j])
        if len(g[i]) > 0:
            g[i].remove(i)

    print(str(g))
    
