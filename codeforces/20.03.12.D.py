n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n):
    a[i] -= b[i]
a.sort(reverse=True)
i,j=0,n-1
tot=0
while i <= j:
    while a[i] + a[j] <= 0 and j > i:
        j -= 1
    tot += j - i
    i += 1
print(tot)
