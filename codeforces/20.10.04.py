from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        l = list(map(int,input().split()))
        l.sort()
        x = l[2]-l[1]-l[0]
        x = max(x, 0) + 1
        print(x)
        

def B():
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        mat=[[] for i in range(n)]
        newMat = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            a = list(map(int,input().split()))
            mat[i] = a
        tot = 0
        for i in range(n//2):
            for j in range(m//2):
                s = sorted([mat[i][j],mat[i][m-j-1],mat[n-i-1][j],mat[n-i-1][m-j-1]])
                dest = round(newMat[i][j]/4)
                dest = max(dest, s[1])
                dest = min(dest, s[2])
                for k in s:
                    tot += abs(k - dest)
        if n % 2 == 1:
            for j in range(m//2):
                dest = (mat[n//2][j] + mat[n//2][m-j-1])//2
                tot += abs(mat[n//2][j] - dest)
                tot += abs(mat[n//2][m-j-1] - dest)
        if m % 2 == 1:
            for i in range(n//2):
                dest = (mat[i][m//2] + mat[n-i-1][m//2])//2
                tot += abs(mat[i][m//2] - dest)
                tot += abs(mat[n-i-1][m//2] - dest)
        print(tot)
            

def C():
    a=list(map(int,input().rstrip()))
    n=len(a)
    mod=10**9 + 7

    dp=[0]*n
    dp[0] = 0
    for i in range(1,n):
        dp[i] = (dp[i-1] + (i * pow(10, i - 1, mod))) % mod
    tot = 0
    for i in range(0, n):
        left = (((n - i - 1) * (n - i) // 2) % mod)
        left = (left * a[n - i - 1] * pow(10, i, mod) % mod)
        right = a[n - i - 1] * dp[i] % mod
        tot = (tot + left + right) % mod
    print(tot)

C()

