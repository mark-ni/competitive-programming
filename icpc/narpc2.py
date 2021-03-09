from sys import stdin
input=stdin.readline

def B():
    n=int(input())
    runners=[[]] * n
    for i in range(n):
        l=list(input().split(' '))
        name=l[0]
        a=float(l[1])
        b=float(l[2])
        runners[i] = [b,a,name]
    runners.sort()

    tot1 = 21
    fastestind = -1
    for i in range(3,n):
        if runners[i][1]< tot1:
            tot1=runners[i][1]
            fastestind = i

    tot1 += runners[0][0] + runners[1][0] + runners[2][0]
    tot2 = runners[0][1] + runners[1][0] + runners[2][0] + runners[3][0]
    tot3 = runners[0][0] + runners[1][1] + runners[2][0] + runners[3][0]
    tot4 = runners[0][0] + runners[1][0] + runners[2][1] + runners[3][0]

    if min([tot1,tot2,tot3,tot4]) == tot1:
        print(tot1)
        print(runners[fastestind][2])
        print(runners[0][2])
        print(runners[1][2])
        print(runners[2][2])
    elif min([tot1,tot2,tot3,tot4]) == tot2:
        print(tot2)
        print(runners[0][2])
        print(runners[1][2])
        print(runners[2][2])
        print(runners[3][2])
    elif min([tot1,tot2,tot3,tot4]) == tot3:
        print(tot3)
        print(runners[1][2])
        print(runners[0][2])
        print(runners[2][2])
        print(runners[3][2])
    else:
        print(tot4)
        print(runners[2][2])
        print(runners[1][2])
        print(runners[0][2])
        print(runners[3][2])

def E():
    from heapq import heappop, heappush
    h,w=map(int,input().split())
    e=[0]*h
    d=[0]*h
    for k in range(h):
        e[k]=list(map(int,input().split()))
        d[k]=[0]*w
    i,j=map(int,input().split())
    i-=1
    j-=1

    coors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    def isLegal(x,y,h,w):
        return x < h and x >= 0 and y < w and y >= 0

    q=[]
    d[i][j] = e[i][j]
    heappush(q,[d[i][j],i,j])
    
    while len(q) > 0:
        drain,x,y=map(int,heappop(q))
        for coor in coors:
            x1,y1=x+coor[0],y+coor[1]
            if isLegal(x1,y1,h,w) and e[x1][y1] - d[x1][y1] < 0 and d[x1][y1] > drain:
                if max(e[x1][y1], drain) < d[x1][y1]:
                    d[x1][y1] = max(e[x1][y1], drain)
                    heappush(q,[d[x1][y1],x1,y1])
    s=-1 * sum([sum(d[_]) for _ in range(h)])
    print(s)

def G():
    from collections import deque
    n,m=map(int,input().split())

    teams=[[0,0] for i in range(n)]
    scores=[set()]*(m+1)
    rank=1
    tiedLowerPen = 0

    scores[0] = set(range(n))
    
    for _ in range(m):
        t,p=map(int,input().split())
        t-=1
        scores[teams[t][0]].remove(t)
        teams[t][0] += 1
        teams[t][1] += p
        scores[teams[t][0]].add(t)

        if t == 0:
            rank -= tiedLowerPen
            tiedLowerPen = 0
            for i in scores[teams[0][0]]:
                if teams[i][1] < teams[0][1]:
                    tiedLowerPen += 1
            rank -= len(scores[teams[0][0]]) - 1 - tiedLowerPen
        else:
            if teams[t][0] == teams[0][0]:
                if teams[t][1] < teams[0][1]:
                    tiedLowerPen += 1
                    rank += 1
            else:
                if teams[t][1] - p < teams[0][1]:
                    tiedLowerPen -= 1
                else:
                    rank += 1
        print(rank)

G()
                
                
    
    

    

    
