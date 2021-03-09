t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    minAdj = max(a)
    maxAdj = min(a)
    if a[0] == -1:
        if a[1] != -1:
            if a[1] > maxAdj:
                maxAdj = a[1]
            if a[1] < minAdj:
                minAdj  = a[1]
    if a[n-1] == -1:
        if a[n-2] != -1:
            if a[n-2] > maxAdj:
                maxAdj = a[n-2]
            if a[n-2] < minAdj:
                minAdj = a[n-2]
    for i in range(1, n-1):
        if a[i] == -1:
            if a[i - 1] != -1:
                if a[i - 1] > maxAdj:
                    maxAdj = a[i - 1]
                if a[i - 1] < minAdj:
                    minAdj = a[i - 1]
            if a[i + 1] != -1:
                if a[i + 1] > maxAdj:
                    maxAdj = a[i + 1]
                if a[i + 1] < minAdj:
                    minAdj = a[i + 1]
    if minAdj == -1 and maxAdj == -1:
        minAdj = 0
        maxAdj = 0
    m = 0
    k = (maxAdj + minAdj)//2
    if a[0] == -1:
        a[0] = k
    for i in range(1,n):
        if a[i] == -1:
            a[i] = k
        m = max(abs(a[i] - a[i - 1]),m)
    print(*[m,k])
