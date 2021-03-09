from sys import stdin
input=stdin.readline

def A():
    from collections import defaultdict
    def invert(n):
        num = list(n[::-1])
        for i in range(len(num)):
            if num[i] == '3' or num[i] == '4' or num[i] == '7':
                return False, int(n)
            elif num[i] == '6':
                num[i] = '9'
            elif num[i] == '9':
                num[i] = '6'
        return True, int(''.join(num))
    n,s=map(int,input().split())
    k=list(input().rstrip().split())
    j=0
    a=defaultdict()
    invertTable=defaultdict()
    
    for i in range(n):
        x=int(k[i])
        a[x] = a.get(x, 0) + 1
        truth,inverted=invert(k[i])
        if truth:
            if inverted != x:
                a[inverted] = a.get(inverted,0) + 1
            invertTable[x] = inverted
            invertTable[inverted] = x
        else:
            invertTable[x] = s - x + 1
    #Exceptions: if a card's inverse is equal to itself
    truth=False
    for i in a.keys():
        if i <= s//2:
            if a.get(s - i, 0) >= 1:
                if invertTable[i] == s - i:
                    if a.get(s - i, 0) >= 2:
                        truth = True
                        break
                else:
                    truth = True
                    break
    if truth: print("YES")
    else: print("NO")
    
def F():
    from collections import defaultdict
    s=''.join(input().rstrip().lower().split())
    alphabet=[chr(x) for x in range(ord('a'),ord('a')+26)]
    letters=defaultdict()
    options=[1,3]
    dic=[]
    for a in options:
        dic.append(a + 0 * 1)
        for b in options:
            dic.append(a+b + 1 * 1)
            for c in options:
                dic.append(a+b+c + 2 * 1)
                for d in options:
                    dic.append(a+b+c+d + 3 * 1)
                    for e in options:
                        dic.append(a+b+c+d+e + 4 * 1)
                        for f in options:
                            dic.append(a+b+c+d+e+f + 5 * 1)
                            for g in options:
                                dic.append(a+b+c+d+e+f+g + 6 * 1)
    dic.sort()
    length=0
    for i in s:
        if i in alphabet:
            letters[i]=letters.get(i,0)+1
            length += 1
    li=list(letters.values())
    li.sort(reverse=True)
    tot=(length-1) * 3
    for i in range(len(li)):
        tot += li[i] * dic[i]
    print(tot)

def G():
    n=int(input())
    k=list(map(int,input().split()))
    i=0
    while len(k) > 2:
        i += (k[i] - 1) % n
        k.pop(i)
        n -= 1
        i %= n
        
        
        
        
        
    
