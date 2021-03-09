import math

def nCr(n, k, p): 
    # initialize numerator 
    # and denominator 
    num = den = 1 
    for i in range(k): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,
            p - 2, p)) % p 

n,m=map(int,input().split(' '))
N = 10**9+7
endsWith = [0]*(n+1)
startsWith = [0]*(n+1)
prod = [0] * (n+1)
for k in range(1,n+1):
    endsWith[k] = nCr(k+m-2,m-1,N)
    startsWith[k] = nCr(m+n-k,m,N)
tot = 0
for i in range(1,n+1):
    tot += (endsWith[i] * startsWith[i]) % N
tot %= N
print(tot)
