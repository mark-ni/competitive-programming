from sys import stdin
input=stdin.readline
def getAns(n,k):
    if n % 2 != k % 2:
        print("NO")
    elif pow(k,2) > n:
        print("NO")
    else:
        print("YES")
    
t=int(input())
d=[0]*pow(10,10)
for _ in range(t):
    n,k=map(int,input().split())
    getAns(n,k)
