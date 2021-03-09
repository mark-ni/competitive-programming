from sys import stdin
input=stdin.readline

def e667():
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        x=sorted(list(map(int,input().split())))
        y=list(map(int,input().split()))

        mostSaved=[0]*(n+1)
        savedFromStart=[0]*n
        i,j=0,0
        prevX = -1
        while i < n:
            if x[i] == prevX:
                savedFromStart[i] = savedFromStart[i - 1]
            else:
                prevX = x[i]
                while j < n and x[j] <= x[i] + k: j += 1
                savedFromStart[i] = j - i
            i += 1    
        for i in range(n-1,-1,-1):
            mostSaved[i] = max(mostSaved[i+1], savedFromStart[i])
        out=[savedFromStart[i] + mostSaved[min(n,i+savedFromStart[i])] for i in range(n)]
        #print(str(savedFromStart))
        #print(str(mostSaved))
        #print(str(out))
        print(max(out))
        
def c668():
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        s=list(input().rstrip())
        b=['?']*k
        truth=True
        for i in range(n):
            c=s[i]
            if c != b[i % k]:
                if b[i % k] == '?':
                    b[i % k] = c
                else:
                    if c != '?':
                        truth=False
                        break
        if not truth: print("NO")
        else:
            #print(_,": ",str(b))
            arr=[0,0]
            for i in b:
                if i == '1': arr[1] += 1
                elif i == '0': arr[0] += 1
            if max(arr) <= k//2: print("YES")
            else: print("NO")
c668()
                
    
    
        
        
    
    
    
