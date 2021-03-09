from sys import stdin
input=stdin.readline
n,a,b,k=map(int,input().split())
h=list(map(int,input().split()))
secret=[0]*n
for i in range(n):
    m = (h[i] - 1) % (a + b) + 1
    secret[i] = (m-1)//a
secret.sort()
pts = 0
while k > 0 and pts < n:
    k -= secret[pts]
    if k >= 0:
        pts += 1
print(pts)
    
    
