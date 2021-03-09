n = int(input())
l = [0] * n * 2
for i in range(n):
    l[2 * i], l[2 * i + 1] = map(int,input().split(' '))
#print(*l)

ins = [0] * n
outs = [0] * n

def isSol(pairs):
    for i in range(0, n, 2):
        ins[pairs[i]] = pairs[i+1]
        ins[pairs[i+1]] = pairs[i]
    for i in range(n):
        pt = [l[2*i + 1], l[2 * i]]
        closest = -1
        currOut = -1
        for j in range(0, n):
            if l[2*j + 1] == pt[0]:
                if l[2*j] - pt[1] > 0:
                    if l[2*j] - pt[1] < closest or closest < 0:
                        currOut = j
                        closest = l[2*j] - pt[1]
        outs[i] = currOut
    #print(*pairs)
    #print(*ins)
    #print(*outs)
    #print()
    for i in range(n):
        start = i
        curr = outs[ins[start]]
        while True:
            if curr == -1:
                break
            elif curr == start:
                return 1
            curr = outs[ins[curr]]

def p(n):
    if (n==2):
        yield [0, 1]
    else:
        Sn_2 = p(n-2) 
        for s in Sn_2:
            yield( s + [n-2,n-1] )
            for i in range(0, (n - 1)//2):
                sn = list(s)
                sn.remove(s[2*i])
                sn.remove(s[2*i + 1])
                yield( sn + [s[2*i],  n-2, s[2*i + 1], n-1] )
                yield( sn + [s[2*i + 1], n-2, s[2 * i], n-1] )

#tot = 0
#for i in p(n):
#    if isSol(i):
#        tot += 1
#print(tot)




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
    if f(cap, odd) < num:
        odd -= 2
    return max(odd, even)

asdf = [int(x) for x in input().split(' ')]
print(getAns(asdf[0],asdf[1]))
