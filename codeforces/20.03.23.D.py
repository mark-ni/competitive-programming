n=int(input())
li=[0]*n
li[n-1] = 10
mod=998244353
tenMult=1
for i in range(n-2,-1,-1):
    li[i] = (2 * (tenMult * 10) * 9 + (tenMult) * 81 * (n - 2 - i))%mod
    tenMult *= 10
    tenMult %= mod
print(*li)
