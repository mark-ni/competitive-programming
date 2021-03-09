from sys import stdin,stdout
input=stdin.readline
n,m=map(int,input().split())
l=list(map(int,input().split()))
if l[-1] + m > n + 1 or sum(l) < n: print(-1)
else:
    emptys = n - (m + l[-1]) + 1
    i=0
    if l[0] > emptys:
        i=emptys+2
        emptys=0
    else:
        i=l[0]+1
        emptys -= l[0] - 1
    stdout.write('1')
    for k in range(1,m):
        stdout.write(' ' + str(i))
        if l[k] > emptys:
            i += emptys
            emptys = 0
        else:
            i += l[k] - 1
            emptys -= l[k] - 1
        i += 1

    
            
        
