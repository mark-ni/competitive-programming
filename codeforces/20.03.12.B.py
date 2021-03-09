from sys import stdin
input=stdin.readline
def getAns(n,a):
    for i in range(n - 2):
        for j in range(i + 2, n):
            if a[i] == a[j]:
                return True
    return False
    
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if getAns(n,a): print("YES")
    else: print("NO")
        
