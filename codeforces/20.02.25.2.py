n,d=map(int,input().split())
friends=[[] for i in range(n)]
for i in range(n):
    m,s=map(int,input().split())
    friends[i] = [m,s]
friends.sort()
li=[0]*n
i,j=0,0
tot = 0
while i < n:
    currI = friends[i]
    tot += currI[1]
    while currI[0] - friends[j][0] >= d:
        tot -= friends[j][1]
        j += 1
    li[i] = tot
    i += 1
print(max(li))
