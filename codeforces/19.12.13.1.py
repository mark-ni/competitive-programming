from sys import stdin
import math

input = stdin.readline

n = int(input())
for i in range(n):
    k = int(input())
    print(math.floor(math.log(k, 10)) * 9 + k//(int((math.floor(math.log(k, 10)) + 1) * '1')))