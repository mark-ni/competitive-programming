n = int(input())

for i in range(n):
    asdf = [int(x) for x in input().split(' ')]
    bi = list(input())
    l = asdf[0]
    k = asdf[1]
    
    onesStart = 0
    ci = 0
    
    while k > 0 and ci < l:
        if bi[ci] == '0':
            if k < ci - onesStart:
                onesStart = ci - k
                k = 0
            else:
                k -= ci - onesStart
            temp = bi[ci]
            bi[ci] = bi[onesStart]
            bi[onesStart] = temp
            onesStart += 1
        ci += 1
    
    print("".join(bi))
