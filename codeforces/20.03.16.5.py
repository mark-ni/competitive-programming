#from sys import stdin
#input=stdin.readline
import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n,m=map(int,input().split())
p=list(range(n))
maxs=list(range(n))

#def find(x):
#    if p[x] != x:
#        p[x] = find(p[x])
#    return p[x]

def find(x):
    a2=a
    while p[a2] != a2:
        a2 = p[a2]
    while p[a] != a:
        a = p[a]
        p[a] = a2
    return a

def union(x,y):
    x,y=find(x),find(y)
    if x==y:
        return
    if x > y: x,y = y,x
    p[y]=x
    maxs[x]=max(maxs[y], maxs[x])
    
for i in range(m):
    u,v=map(int,input().split())
    union(u-1,v-1)

ind=0
tot=0
while ind < n:
    if maxs[ind] != p[ind]:
        placeholdInd = ind
        while ind < maxs[placeholdInd]:
            if find(ind) != placeholdInd:
                tot += 1
                union(ind, placeholdInd)
            ind += 1
    ind += 1
print(tot)
