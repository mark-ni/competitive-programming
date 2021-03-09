from sys import stdin
input=stdin.readline
def getAns(n,p):
    visited=[False]*(n+1)
    index=-1
    for i in range(n):
        j=1
        while j < p[i][0] + 1 and visited[p[i][j]]:
            j+=1
        if j == p[i][0] + 1:
            index=i
        else:
            if p[i][0] > 0:
                visited[p[i][j]]=True
    #print(*visited)
    if index < 0:
        print("OPTIMAL")
        return
    else:
        for k in range(1,n+1):
            if not visited[k]:
                print("IMPROVE")
                print(*[index+1,k])
                return
t=int(input())
for _ in range(t):
    n=int(input())
    p=[[] for i in range(n)]
    for i in range(n):
        g=list(map(int,input().split()))
        #k=[0]
        p[i]=g
    getAns(n,p)
