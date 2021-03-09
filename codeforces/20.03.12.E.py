from sys import stdin
input=stdin.readline
n,h,l,r=map(int,input().split())
a=list(map(int,input().split()))

def isGood(t):
    if l <= r:
        if t >= l and t <= r:
            return True
    elif t <= r or t >= l:
        return True
    return False

def printRow(q):
    for row in q:
        print(str(row))
    print()

q=[[-1 for i in range(n + 1)] for j in range(n)]
q[0][0]=a[0]
for row in range(1,n):
    q[row][0]=(a[row] + q[row - 1][0]) % h
for col in range(1,n+1):
    for row in range(col - 1, n):
        q[row][col] = (q[row][col - 1] - 1) % h

for row in range(n):
    for col in range(n + 1):
        if isGood(q[row][col]):
            q[row][col]=1
        else:
            q[row][col]=0

for row in range(1,n):
    q[row][0] += q[row - 1][0]
for col in range(1, n+1):
    for row in range(1, n):
        q[row][col] += max(q[row - 1][col],q[row-1][col-1])

print(max(q[n-1]))


            

        
