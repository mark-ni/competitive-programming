n = int(input())
import math
 
def getdb(s, x):
    l = 1
    length = len(s)
    newS = s + [0] * (3*x - length)
    while length < x and l <= x:
        #newS = newS[0:l] + newS[l - 1] * newS[l:]
        i = length - l
        j = length
        for k in range(newS[l - 1] - 1):
            newS[j:j + i] = newS[l:l + i]
            j += i
            length += i
        l += 1
    return newS[0:length]
 
for i in range(n):
    x = int(input())
    s = [int(x) for x in input()]
    
    dbli = getdb(s,x)
    tot = len(s)
    l = 1
    while l <= x:
        if (tot <= l):
            tot += 10**9 + 7
        tot = l + dbli[l - 1]*(tot - l)
        if math.log(tot) > 9.01:
            tot %= (10**9 + 7)
        l += 1
    print(tot % (10**9 + 7))