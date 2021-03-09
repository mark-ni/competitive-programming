from sys import stdin, stdout
input = stdin.readline


n = int(input())
for _ in range(n):
    n, p, k = map(int, input().split(' '))
    prices = sorted(list(map(int, input().split(' '))))
    
    deals = prices.copy()
    if n >= k:
        for i in range(k - 1):
            deals[i] = sum(deals[0:i+1])
        for i in range(k, n):
            for j in range(i % k, i, k):
                deals[i] += deals[j]
    else:
        for i in range(n):
            deals[i] = sum(deals[0:i+1])
    s = 0
    for i in range(n):
        if deals[i] > p:
            s = i
            break
    if p >= deals[n - 1]:
        s = n
    stdout.write(str(s) + "\n")        
        
    
