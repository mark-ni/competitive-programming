from sys import stdin
import math
input = stdin.readline

t = int(input())

def getAns(n, a):
    s = sum(a)
    curr = a[0]
    for i in range(1, n):
        curr = a[i] ^ curr
    if s - (curr*2) == 0:
        print(0)
        print()
        return
    xor = curr^(3*s)
    nextele = curr^xor
    s += nextele
    d = ((xor)*2 - s)//2
    print(3)
    print(*[nextele,d,d])

for _ in range(t):
    getAns(int(input()), list(map(int, input().split(' '))))
