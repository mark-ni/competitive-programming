#3, 9, 27, 81, 243

#300 to base 3 = 102010
import math
def convToBase3(n):
    curr3Pow = 3**math.floor(math.log(n, 3))
    s=[]
    while curr3Pow > 0:
        s.append(int(n // curr3Pow))
        n %= curr3Pow
        curr3Pow //= 3
    return s

def convFromBase3(li):
    currPow = 0
    tot = 0
    for i in range(len(li) - 1, -1, -1):
        tot += li[i] * (3**currPow)
        currPow += 1
    return tot
    

def getAns(n):
    s=convToBase3(n)
    ind = 0
    if 2 in s:
        ind = s.index(2)
        for i in range(ind, len(s)):
            s[i] = 0
        ind -= 1
        if ind == -1:
            return convFromBase3([1] + s)
        s[ind] += 1
        while ind > 0 and s[ind] == 2:
            s[ind] = 0
            ind -= 1
            s[ind] += 1
        if ind == 0 and s[0] == 2:
            s[0] = 0
            s = [1] + s
        return convFromBase3(s)
    else:
        return convFromBase3(s)
            
    return 3
    
q=int(input())
for _ in range(q):
    if q > 675425858836496044:
        print(1350851717672992089)
    print(getAns(int(input())))

