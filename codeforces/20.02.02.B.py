from sys import stdin
input = stdin.readline    

def getAns(n,a):
    diff = [0]*n
    diff2 = [0]*n
    for i in range(n//2 + 1):
        diff[i] = i
        diff2[n - i - 1] = i
    for i in range(n//2 + 1, n):
        diff[i] = n - i - 1
        diff2[n - i - 1] = n - i - 1
    for i in range(n):
        diff[i] = max(a[i] - diff[i], -1)
        diff2[i] = max(a[i] - diff2[i], -1)
    if -1 not in diff or -1 not in diff2:
        print("Yes")
    else:
        print("No")

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(' ')))
    getAns(n,a)
#n=6,7
#0,1,2,3,4,5
#0,1,2,3,1,0
#0,1,2,3,2,1,0
    
