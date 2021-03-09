from sys import stdin
input=stdin.readline

def getAns(n,m,d):
    b=[0]*(m)
    for i in d:
        b[i % m] += 1
        if b[i % m] == 2:
            return 0
    #print(str(c))
    prod = 1
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            #print(abs(d[i]-d[j]) % m)
            prod *= (abs(d[i] - d[j]) % m)
            prod %= m
    return prod
    

n,m=map(int,input().split())
d=list(map(int,input().split()))
print(getAns(n,m,d))
