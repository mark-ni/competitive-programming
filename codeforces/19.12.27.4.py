from sys import stdin
import math
input = stdin.readline

n = int(input())
prescount = [0] * (10**6 + 1)
big = 998244353

for _ in range(n):
    l = list(map(int, input().split(' ')))
    for i in range(1, l[0] + 1):
        prescount[l[i]] += 1
prod = 0
for i in range(1, 10**6 + 1):
    prod += prescount[i] * prescount[i]
    if math.log10(prod) > 8.9:
        prod %= big
n2 = pow(n,2,big)
print((prod * (pow(n2,big-2,big)))%big)
