from sys import stdin
input=stdin.readline

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    visited=[False]*(204)
    for i in a:
        visited[i]=True
    i = 1
    while x >= 0 and i < 204:
        if visited[i] == False:
            x -= 1
            visited[i] = True
        i += 1
    
    print(i - 2)

    
