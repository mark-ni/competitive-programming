from sys import stdin
input = stdin.readline

n,q=map(int,input().split(' '))
rows = [[True]*(n+3),[True]*(n+3)]
prev=True
s=set()
for _ in range(q):
    r,c=map(int,input().split(' '))
    rows[r-1][c] = not rows[r-1][c]
    if rows[r-1][c]:
        if (rows[r-1][c-2] and rows[r-1][c-1]) or (rows[r-1][c-1] and rows[r%2][c-1] and rows[r%2][c-2]):
            s.discard(c-1)
        if (rows[r-1][c-1] and rows[r-1][c+1]) or (rows[r-1][c+1] and rows[r%2][c] and rows[r%2][c-1]) or (rows[r-1][c-1] and rows[r%2][c] and rows[r%2][c+1]):
            s.discard(c)
        if (rows[r-1][c+1] and rows[r-1][c+2]) or (rows[r-1][c+1] and rows[r%2][c+1] and rows[r%2][c+2]):
            s.discard(c+1)
    else:
        if not (rows[r%2][c-1] and rows[r%2][c] and rows[r%2][c+1]):
            s.add(c)
    if len(s) == 0:
        print("Yes")
    else:
        print("No")
        
    
    #currRow = 0
    #currCol = 1
    #while currCol < n:
    #    if rows[currRow][currCol+1]:
    #        currCol += 1
    #    elif rows[currRow][currCol] and rows[currRow][currCol+1] and rows[currRow][currCol+2]:
    #        currCol += 2
    #        currRow ^= 1
    #    else:
    #        break
    #if currCol >= n:
    #    print("Yes")
    #else:
    #    print("No")
    
    
