T = int(input())
for _ in range(T):
    n,x=map(int,input().split())
    s=list(map(int,input()))
    balanceList = [s[0]*(-2) + 1]*n
    for i in range(1,n):
        if (s[i] == 0):
            balanceList[i] = balanceList[i - 1] + 1
        else:
            balanceList[i] = balanceList[i - 1] - 1
    baseB = balanceList[n - 1]

    if baseB == 0:
        for i in balanceList:
            if i == x:
                print(-1)
                break
        print(0)
    else:
        #[1,0,1,2,1,2], n = 10
        #[-1,-2,-1,0,-1,0]
        newBalance = balanceList + balanceList + balanceList
        for i in range(n):
            newBalance[i] -= baseB
        for i in range(2*n, 3*n):
            newBalance[i] += baseB
        tot = 0
        for i in newBalance:
            if i == x % baseB:
                tot += 1
        print(tot)
    
