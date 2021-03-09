import math

def prod(li):
    p = 1
    for i in li: p*=i
    return p

def getAns(n):
    d = dict()
    while n % 2 == 0:
        if 2 in d.keys():
            d[2] += 1
        else:
            d[2] = 1
        n//=2
    for i in range(3, int(math.sqrt(n)) + 3, 2):
        while n % i == 0:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
            n//=i
    if n > 2:
        d[n] = 1
    k = list(d.keys())
    if len(k) >= 3:
        a = k[0]**d[k[0]]
        b = k[1]**d[k[1]]
        c = prod([(k[i]**d[k[i]]) for i in range(2, len(k))])
    elif len(k) == 2:
        if d[k[0]] >= 3:
            a = k[0]
            b = k[0]**(d[k[0]] - 1)
            c = k[1]**(d[k[1]])
        else:
            if d[k[1]] >= 3:
                a = k[0]**d[k[0]]
                b = k[1]
                c = k[1]**(d[k[1]] - 1)
            elif d[k[1]] == 2 and d[k[0]] == 2:
                a = k[0]
                b = k[1]
                c = k[0]*k[1]
            else:
                return False, -1, -1, -1
    else:
        if d[k[0]] >= 6:
            a = k[0]
            b = k[0] * k[0]
            c = k[0]**(d[k[0]] - 3)
        else:
            return False, -1, -1, -1
    return True, a, b, c

for _ in range(int(input())):
    n = int(input())
    truth,a,b,c = getAns(n)
    if truth:
        print("YES")
        print(*sorted([a,b,c]))
    else:
        print("NO")
        
    
