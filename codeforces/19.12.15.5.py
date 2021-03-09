#from sys import stdin, stdout
import math
#from collections import deque

#input = stdin.readline
def f(cap, num):
    if num % 2 == 0:
        num //= 2
        even = 1
    else:
        even = 0
    k = math.floor(math.log2(cap / num))
    facts = 2**k
    return facts - 1 + min(facts, cap - num * facts + 1) - even

def getAns(cap, num):
    #oddSol
    k = math.floor(math.log2(num))
    effB = 2**k
    odd = math.floor((cap - (num - effB))/(effB))
    #evenSol
    num += 1
    k = math.floor(math.log2(num))
    effB = 2**k
    even = math.floor((cap - (num - effB))/(effB) * 2)
    if even % 2 == 1:
        even += 1
    if f(cap, even) < num - 1:
        even -= 2
    if odd % 2 == 0:
        odd += 1
    if f(cap, odd) < num - 1:
        odd -= 2
    return max(odd, even)

asdf = [int(x) for x in input().split(' ')]
a = asdf[0]
b = asdf[1]
print(getAns(a,b))

