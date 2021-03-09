def getAns(n,m):
    mod=998244353
    rowM = [1]*(m+1)
    for i in range(1, m+1):
        rowM[i] = (rowM[i - 1] * (m - i + 1) // i) % mod

    diagN = [0]*(n)
    diagN[0] = (rowM[n] * n // m) % mod
    for i in range(1,n):
        diagN[i] = (diagN[i - 1] * (n - i) // (m - i)) % mod
    tot=0
    for k in range(n):
        tot += rowM[k] * diagN[k]
        tot %= mod
    tot *= 2
    tot -= rowM[0] * diagN[0]
    tot -= rowM[n - 1] * diagN[n - 1]
    tot %= mod
    print(str(rowM))
    print(str(diagN))
    print(tot)

n,m=map(int,input().split())
getAns(n,m)
