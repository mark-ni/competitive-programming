from sys import stdin
input=stdin.readline

def A():
    for _ in range(int(input())):
        a,b,c,d=map(int,input().split())
        print(b,c,c)
    return

def B():
    for _ in range(int(input())):
        x,n,m=map(int,input().split())
        while x > 20 and n > 0:
            x = x//2 + 10
            n -= 1
        if x <= 10 * m: print("YES")
        else: print("NO")
    return

def C():
    from collections import deque
    n,k=map(int,input().split())
    d=[set() for i in range(n+1)]
    a=[0]*(n+1)
    for i in range(n-1):
        u,v=map(int,input().split())
        d[u].add(v)
        d[v].add(u)
        a[u]+=1
        a[v]+=1
    #find how deep each node is
    queue = deque([1])
    visited = [False] * (n + 1)
    heights=[-1]*(n+1)
    heights[1]=0
    while len(queue) > 0:
        e = queue.popleft()
        visited[e] = True
        for i in d[e]:
            if not visited[i]:
                heights[i] = heights[e] + 1
                queue.append(i)
    #find num children of each node
    queue2 = deque()
    numChild=[0]*(n+1)
    visited = [False] * (n + 1)
    for i in range(1, n+1):
        if a[i] == 1 and i != 1:
            parent=d[i].pop()
            numChild[i]=0
            visited[i]=True
            numChild[parent] += 1
            d[parent].remove(i)
            if len(d[parent]) == 1:
                queue2.append(parent)
    
    while len(queue2) > 0:
        curr=queue2.popleft()
        if len(d[curr]) == 1 and curr != 1:
            parent = d[curr].pop()
            numChild[parent] += numChild[curr] + 1
            d[parent].remove(curr)
            if len(d[parent]) == 1:
                queue2.append(parent)
    numChild[1]=n-1
    #print("Heights: ", *heights)
    #print("Children: ", *numChild)
    #calculate
    scores=[0]*(n)
    for i in range(1, n+1):
        scores[i-1]=heights[i]-numChild[i]
    scores.sort(reverse=True)
    #print(*scores)
    print(sum(scores[0:k]))
    return

def D():
    bestVal=[0]
    def f(x,y,z):
        return (x-y)*(x-y)+(x-z)*(x-z)+(y-z)*(y-z)
    def test(x,y,z):
        if f(x,y,z) < bestVal[0]:
            bestVal[0]=f(x,y,z)
    def run(m,l,h):
        nm,nl,nh=len(m),len(l),len(h)
        mi,li,hi=0,0,0        
        while mi < nm:
            while li < nl and l[li] <= m[mi]:
                li += 1
            li -= 1
            while hi < nh and h[hi] < m[mi]:
                hi += 1
            if li == -1:
                li += 1
            elif hi == nh:
                break
            else:
                test(l[li],m[mi],h[hi])
            mi += 1

    for _ in range(int(input())):
        input()
        r=sorted(list(set(map(int,input().split()))))
        g=sorted(list(set(map(int,input().split()))))
        b=sorted(list(set(map(int,input().split()))))
        bestVal=[f(r[0],g[0],b[0])]
        run(r,g,b)
        run(r,b,g)
        run(g,b,r)
        run(g,r,b)
        run(b,r,g)
        run(b,g,r)
        print(bestVal[0])
    return

D()
