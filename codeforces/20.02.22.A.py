t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    tot = 0
    if a > 0:
        a -= 1
        tot += 1
    if b > 0:
        b -= 1
        tot += 1
    if c > 0:
        c -= 1
        tot += 1
    if (a > 1 and b > 1 and c > 1):
        c -= 2
        b -= 2
        a -= 2
        tot += 3
    elif (a > 1 and b > 0 and c > 0):
        a -= 2
        b -= 1
        c -= 1
        tot += 2
    elif (a > 0 and b > 1 and c > 0):
        a -= 1
        b -= 2
        c -= 1
        tot += 2
    elif (a > 0 and b > 0 and c > 1):
        a -= 1
        b -= 1
        c -= 2
        tot += 2
    elif (a > 0 and b > 0):
        a -= 1
        b -= 1
        tot += 1
    elif (a > 0 and c > 0):
        a -= 1
        c -= 1
        tot += 1
    elif (b > 0 and c > 0):
        b -= 1
        c -= 1
        tot += 1
    if (a > 0 and b > 0 and c > 0):
        tot += 1
    print(tot)
