n,m=map(int,input().split())
k=m
j=1
mod=998244353
for i in range(2,m-1):
    k=(k*(n+i-1)) % mod
for i in range(2,m-1):
    j=(j*i)%mod
print(k,j)
print((k*pow(j,mod-2,mod))%mod)

[1,2,3,4], 5



