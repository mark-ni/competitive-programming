import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n,m,p=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    if a[i] % p != 0:
        c=i
        break
for j in range(m):
    if b[j] % p != 0:
        d=j
        break
print(c+d)
