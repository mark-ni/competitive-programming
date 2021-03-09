from sys import stdin
input=stdin.readline

#from collections import defaultdict
#from collections import deque
#from heapq import heappop, heappush

def A():
    s=list(map(int,input().rstrip()))
    d=[[0 for i in range(10)] for j in range(10)]
    for i in range(len(s)-1):
        a,b=min(s[i],s[i+1]),max(s[i],s[i+1])
        d[a][b] += 1
    
    print('',end='\t')
    print(*list(range(1,10)))
    print()
    print()
    for i in range(1,10):
        print(str(i)+':',end='\t')
        print(*d[i])

def C():
    n=int(input())
    x=[0]*n
    for i in range(n):
        x[i]=int(input())

def D():
    n,m=map(int,input().split())
    for i in range(m):
        s,k=map(str, input().rstrip().split())
        
def J():
    s=input().rstrip()
    if len(set(s)) != len(s): print(0)
    else: print(1)

def K():
    n=int(input())
    s=input().rstrip()
    nums=[0]*10
    for i in range(1,n+1):
        x=i
        while x > 0:
            nums[x % 10] += 1
            x //= 10
    real=[0]*10
    for i in range(10):
        real[i] = s.count(str(i))
    missing=[]
    for i in range(10):
        for j in range(nums[i] - real[i]):
            missing.append(i)
    #print(str(nums))
    #print(str(real))
    #print(str(missing))
    if len(missing) == 1:
        print(missing[0])
    elif len(missing) == 2:
        if missing[0] == missing[1]:
            print(11 * missing[0])
        else:
            if str(10 * missing[0] + missing[1]) in s:
                print(10 * missing[0] + missing[1])
            else:
                print(10 * missing[1] + missing[0])
    else:
        print(100)

def K():
    n=int(input())
    s=input().rstrip()
    ind=0
    ans=n
    for i in range(1,n):
        l=len(str(i))
        if int(s[ind:ind+l]) != i:
            ans = i
            break
        else:
            ind += l
    print(ans)

def N():
    n=int(input())
    l=[0]*n
    for i in range(n):
        l[i]=int(input())
    l.sort()
    tot=0
    lim=0
    for i in range(0,n-2):
        for j in range(i + 1, n - 1):
            lim = j+1
            while lim < n and l[lim] < l[i] + l[j]:
                lim += 1
            if lim - j >= 2:
                tot += 2**(lim - j - 1) - 1
    print(tot)

def L():
    mod=998244353
    def count(x):
        tot=0
        length=len(x)
        isValid=0
        for j in [pow(9,i,mod) for i in range(0, length)]:
            tot = (tot + j) % mod
        #^should be same as
        #for j in range(length):
        #   tot = (tot + pow(9,j,mod)) % mod
        tot = (tot + ((x[0] - 1)*pow(9,length-1,mod))) % mod
        for i in range(1, length):
            z=x[i]
            if x[i-1] < x[i]:
                z -= 1
            tot = (tot + z*pow(9,length-i-1,mod)) % mod
            if i > 0 and x[i-1] == x[i]:
                break
        return tot
    def check(x):
        for i in range(1,len(x)):
            if x[i] == x[i-1]:
                return 0
        return 1
    l=list(map(int,input().rstrip()))
    u=list(map(int,input().rstrip()))
    print((count(u) + check(u) - count(l)) % mod)
    
def B():
    n,c=map(int(input().split()))
    dp=[0]*c
    k=[0]*n
    for i in range(n):
        k[i]=int(input())
    k.sort()
    s=sum(k)
    
    
    currSmallest=k[0]
    i=0
