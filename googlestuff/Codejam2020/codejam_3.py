from sys import stdin
input=stdin.readline

def getAns():
    r,c=map(int,input().split())
    if r == 1 and c == 1:
        return input().rstrip()
    s=[0 for i in range(r)]
    for i in range(r):
        q=list(map(int,input().split()))
        s[i]=q
    did=True
    score=0
    while did:
        did=False
        g=[[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if s[i][j] != -1:
                    score += s[i][j]
                g[i][j]=s[i][j]
        for i in range(r):
            for j in range(c):
                if g[i][j] != -1:
                    north=i
                    south=i
                    east=j
                    west=j
                    n=0
                    Sum=0
                    while north > 0:
                        north -= 1
                        if g[north][j] != -1:
                            n+=1
                            Sum+=g[north][j]
                            break
                    while south < r - 1:
                        south += 1
                        if g[south][j] != -1:
                            n+=1
                            Sum += g[south][j]
                            break
                    while west > 0:
                        west -= 1
                        if g[i][west] != -1:
                            n += 1
                            Sum += g[i][west]
                            break
                    while east < c - 1:
                        east += 1
                        if g[i][east] != -1:
                            n += 1
                            Sum += g[i][east]
                            break
                    if g[i][j] * n < Sum:
                        did=True
                        s[i][j] = -1
    return str(score)

t=int(input())
for _ in range(t):
    print('Case #' + str(_+1) + ': ' + str(getAns()))
            
        
            
        
        
            
    
    
    
