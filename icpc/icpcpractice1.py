from sys import stdin
input=stdin.readline

def A():
    from collections import deque
    
    n=int(input())
    s=[0]*n
    for i in range(n):
        s[i]=input().rstrip().split()
    g=[set() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if s[i][1] in s[j][1:]:
                    g[i].add(j)
    size=[0]*n
    seens=[0]*n
    stack=deque()
    for i in range(n):
        seen=[0]*n
        stack.append(i)
        while len(stack) > 0:
            curr=stack.popleft()
            seen[curr]=1
            for j in g[curr]:
                if seen[j] == 0:
                    stack.appendleft(j)
        seens[i] = seen.copy()
    for i in range(n):
        for j in range(n):
            if seens[i][j] == 1 and seens[j][i] == 1:
                size[i] += 1
    print(n - max(size))  
        
        
def C():
    def il(a,b):
        if a < 0 or b < 0 or a > 7 or b > 7:
            return False
        return True
    
    board=[0 for i in range(8)]
    queens=0
    for i in range(8):
        board[i] = input().rstrip()
    valid=True
    moves=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    for i in range(8):
        for j in range(8):
            if board[i][j] == "*":
                queens += 1
                for dx,dy in moves:
                    x,y=i,j
                    while il(x+dx,y+dy):
                        x,y=x+dx,y+dy
                        if board[x][y] == "*":
                            valid = False
    if queens != 8:
        valid = False
    if valid: print("valid")
    else: print("invalid")
        
def D():
    w,p=map(int,input().split())
    l=[0] + list(map(int,input().split())) + [w]
    t=[False]*(w+1)
    for i in range(p + 2):
        for j in range(i + 1, p + 2):
            t[l[j] - l[i]] = True
    ans=[]
    for i in range(len(t)):
        if t[i]:
            ans.append(i)
    print(*ans)

def F():
    t=int(input())
    for _ in range(t):
        s=input().rstrip()
        if len(s) >= 10:
            if s[:10] == "Simon says":
                print(s[10:])

def H():
    x,y=map(int,input().split())
    code=[0]+list(map(int,input().rstrip()))
    c=len(code)
    grid=[0 for i in range(y)]
    for i in range(y):
        grid[i]=list(map(int,input().rstrip()))
    dp=[[0 for i in range(x)] for j in range(y)]
    for i in range(y):
        for j in range(x):
            dp[i][j]=[2000]*c
    #No code
    #start square
    dp[y-1][0][0] = grid[y-1][0]
    #bottom row
    for j in range(1,x):
        v = grid[y-1][j]
        dp[y-1][j][0] = v + dp[y-1][j-1][0]
        for k in range(1,c):
            gap=code[k]+1
            if j >= gap:
                dp[y-1][j][k] = v + min(dp[y-1][j-gap][k-1],dp[y-1][j-1][k])
    #left column
    for i in range(y-2,-1,-1):
        v = grid[i][0]
        dp[i][0][0] = v + dp[i+1][0][0]
        for k in range(1,c):
            gap=code[k]+1
            if y - i > gap:
                dp[i][0][k] = v + min(dp[i+gap][0][k-1],dp[i+1][0][k])
    #body
    for i in range(y-2,-1,-1):
        for j in range(1,x):
            v=grid[i][j]
            dp[i][j][0] = v + min(dp[i][j-1][0],dp[i+1][j][0])
            for k in range(1,c):
                gap=code[k]+1
                a,b=dp[i][j-1][k],dp[i+1][j][k]
                if j >= gap:
                    a = min(a,dp[i][j-gap][k-1])
                if y - i > gap:
                    b = min(b,dp[i+gap][j][k-1])
                dp[i][j][k] = v + min(a,b)
    print(min(dp[0][x-1]))
    
A()
