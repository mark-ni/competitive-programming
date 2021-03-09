n = int(input())

def getAns(li):
    li.sort()
    total = li[0]
    
    r = li[0]
    s = li[1]
    t = li[2]
    
    a = t - s
    
    if a >= r:
        total += s
        print(total)
        return
    else:
        t -= a
        r -= a
        total += s - (r + 1)//2
        print(total)
        return
    
for i in range(n):
    getAns([int(x) for x in input().split(' ')])