from sys import stdin,stdout
input=stdin.readline
n,m,k=map(int,input().split())        
#for i in range(k):
#    sx,sy=map(int,input().split())
#for i in range(k):
#    fx,fy=map(int,input().split())
print(n * m + n + m - 3)
for i in range(n - 1):
    stdout.write('D')
for i in range(m - 1):
    stdout.write('L')
for i in range(n - 1):
    stdout.write('U')
for i in range(1, m):
    stdout.write('R')
    if i % 2 == 1:
        for j in range(n - 1):
            stdout.write('D')
    else:
        for j in range(n - 1):
            stdout.write('U')
    
