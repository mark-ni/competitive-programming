def tInput():
    from sys import stdin
    input=stdin.readline
tInput()


def A():
    for _ in range(int(input())):
        n,k=map(int,input().split())
        if n>=k: print(int(n%2!=k%2))
        else: print(k-n)
def B():
    for _ in range(int(input())):
        x1,y1,z1=map(int,input().split())
        x2,y2,z2=map(int,input().split())
        tot=0
        p=min(x1,z2)
        x1 -= p
        z2 -= p        
        tot+=2*min(z1,y2)
        p=min(z1,y2)
        z1-=p
        y2-=p
        if z2 > 0:
            z2 -= min(z2,z1)
            tot-= 2*min(y1,z2)
        print(tot)
def C():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        sa=sorted(a)
        m=min(a)
        w=True
        for i in range(n):
            if a[i]%m != 0:
                if a[i] != sa[i]:
                    w=False
                    break
        if w: print("YES")
        else: print("NO")
def D():
    t=int(input())
    from collections import deque
    for _ in range(t):
        n=int(input())
        graph=[set() for i in range(n+1)]
        graph[1].add(0)
        queue=deque()
        #count the number of nodes below and above each edge. multiply these together and sort
        numChildren=[0]*(n+1)
        
        for i in range(n-1):
            u,v=map(int,input().split())
            graph[u].add(v)
            graph[v].add(u)
        for i in range(1,n+1):
            if len(graph[i]) == 1 and i != 1:
                queue.append(i)
        while len(queue) > 0:
            curr=queue.popleft()
            if curr == 1:
                break
            parent=graph[curr].pop()
            numChildren[curr] += 1
            numChildren[parent] += numChildren[curr]
            graph[parent].remove(curr)
            if len(graph[parent]) == 1:
                queue.append(parent)

        mults=[0]*(n-1)
        for i in range(2,n+1):
            mults[i-2]=numChildren[i]*(n - numChildren[i])
        mults.sort()
        mod=10**9+7
        m=int(input())
        p=list(map(int,input().split()))
        if m <= n - 1:
            p = p + [1]*(n-m-1)
            p.sort()
        else:
            p.sort()
            for i in range(n - 1, m):
                p[n-2] = (p[n-2] * p[i]) % mod
        tot=0
        for i in range(n-1):
            tot = (tot + p[i]*mults[i]) % mod
        print(tot)


def A2():
    t=int(input())
    for _ in range(t):
        d=[0]*26
        n=int(input())
        for j in range(n):
            for i in input().rstrip():
                d[ord(i)-ord('a')] += 1
        truth = True
        for i in range(26):
            if d[i] % n != 0:
                truth = False
                break
        if truth: print("YES")
        else: print("NO")

def B2():
    n=int(input())
    a=sorted(list(map(int,input().split())))
    baseCost=sum(a)-n
    c=2
    cost=0
    while True:
        cost=0
        for i in range(n):
            cost += abs(a[i] - c**i)
        if cost < baseCost:
            c += 1
            baseCost = cost
        else:
            break
    print(baseCost)
        
def C2():
    n=int(input())
    a=list(map(int,input().split()))

    if n == 1:
        print(1,1)
        print(-1*a[0])
        print(1,1)
        print(0)
        print(1,1)
        print(0)
        return
    
    k=[((n - 1) - (a[i] % (n - 1))) * n for i in range(n)]
    print(1,n)
    print(*k)
    print(1,1)
    print(-1*(k[0] + a[0]))
    print(2,n)
    print(*[-1*(k[i] + a[i]) for i in range(1,n)])

def D2():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        Tturn=True
        lastPicked=False
        while a[n-2] > 0:
            if lastPicked: a[n-2] -= 1
            else: a[n-1] -= 1
            Tturn = not Tturn
            lastPicked = not lastPicked
            a.sort()
        if Tturn: print("T")
        else: print("HL")

D2()
        
            
            
        
