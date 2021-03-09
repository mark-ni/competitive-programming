from sys import stdin
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=[ord(x)-ord('a') for x in input().rstrip()]
    p=map(int,input().split())
    alphabet=[0]*26
    twod=[[0 for j in range(26)] for i in range(n)]
    twod[0][s[0]] += 1
    for i in range(1, n):
        for j in range(26):
            twod[i][j]=twod[i-1][j]
        twod[i][s[i]] += 1
    for i in p:
        for j in range(26):
            alphabet[j] += twod[i - 1][j]
    for i in s:
        alphabet[i] += 1
    print(*alphabet)

        
    
    
        
    
