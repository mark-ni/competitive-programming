from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a.sort()
        found=False
        if a[0]+a[1] <= a[n-1]: print(1,2,n)
        else: print(-1)
        

def B():
    from collections import deque
    t=int(input())
    for _ in range(t):
        s=[int(x) for x in input().rstrip()]
        d=deque()
        curr=s[0]
        streak=s[0]
        for i in range(1,len(s)):
            if s[i] != curr:
                if curr == 1:
                    d.append(streak)
                curr = s[i]
                streak = 1
            elif curr == 1:
                streak += 1
        if curr==1: d.append(streak)
        d=list(d)
        d.sort(reverse=True)
        tot=0
        for i in range(0, len(d),2):
            tot += d[i]
        print(tot)


def C():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[int(x)-1 for x in (input().rstrip())]
        d=[0 for i in range(n*10)]
        t=n
        d[t]=1
        for i in range(n):
            t += a[i]
            d[t] += 1
        tot = 0
        for i in d:
            if i >= 2:
                tot += i * (i-1) // 2
        print(tot)
    
        
        

def D():
    from collections import deque
    R,G,B=map(int,input().split())
    arr=[R,G,B]
    r=list(map(int,input().split()))
    g=list(map(int,input().split()))
    b=list(map(int,input().split()))
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)
    r,g,b=deque(r),deque(g),deque(b)

    tot = 0
    
    reachTheEnd=0
    while reachTheEnd < 2:
        if reachTheEnd == 0:
            x,y,z=r[0]*g[0],r[0]*b[0],g[0]*b[0]
            if max(x,y,z) == x:
                tot += x
                r.popleft()
                g.popleft()
                arr[0],arr[1]=arr[0]-1,arr[1]-1
            elif max(x,y,z) == y:
                tot += y
                r.popleft()
                b.popleft()
                arr[0],arr[2]=arr[0]-1,arr[2]-1
            else:
                tot += z
                g.popleft()
                b.popleft()
                arr[1],arr[2]=arr[1]-1,arr[2]-1
        else:
            if arr[0] == 0:
                tot += g[0]*b[0]
                g.popleft()
                b.popleft()
                arr[1],arr[2]=arr[0]-1,arr[2]-1
            elif arr[1] == 0:
                tot += r[0]*b[0]
                r.popleft()
                b.popleft()
                arr[0],arr[2]=arr[0]-1,arr[2]-1
            else:
                tot += g[0]*r[0]
                r.popleft()
                g.popleft()
                arr[0],arr[1]=arr[0]-1,arr[1]-1
        reachTheEnd += sum([int(w==0) for w in arr])                
    print(tot)
        
D()
