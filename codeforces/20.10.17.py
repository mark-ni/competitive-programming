from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        x1,y1,x2,y2=map(int,input().split())
        if x2 == x1:
            print(abs(y2 - y1))
        elif y1 == y2:
            print(abs(x2 - x1))
        else:
            print(abs(x2 - x1) + abs(y2 - y1) + 2)

def B():
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=list(input().rstrip())
        #nonreturnables
        rl,ll,lr,rr=0,0,0,0
        lcount,rcount = 0,0
        for i in range(0, n - 1):
            if s[i] == '<':
                if s[i + 1] == '>':
                    lr += 1
                elif s[i + 1] == '<':
                    ll += 1
                lcount += 1
            elif s[i] == '>':
                if s[i + 1] == '>':
                    rr += 1
                elif s[i + 1] == '<':
                    rl += 1
                rcount += 1
        #check corners
        if s[n - 1] == '<':
            if s[0] == '<': ll += 1
            elif s[0] == '>': lr += 1
            lcount += 1
        elif s[n - 1] == '>':
            if s[0] == '<': rl += 1
            elif s[0] == '>': rr += 1
            rcount += 1

        if lcount == 0 or rcount == 0:
            print(n)
        else:
            print(n - ll - lr - rl - rr)
        

def C():
    t=int(input())
    for _ in range(t):
        s=list(input().rstrip())
        n=len(s)
        i=0
        remaining = 0
        depth=0
        j = n - 1
        while j >= i:
            if s[j] == 'A':
                depth += 1
                if depth > 0:
                    remaining += 1
                    depth = 0
            else:
                depth -= 1
            j -= 1
        remaining += (depth % 2)
        print(remaining)

def D():
    from collections import deque
    n=int(input())
    a=list(map(int,input().split()))
    cols = [[]] * (n)
    filledCols = deque()
    #handle 1s
    k = n - 1
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            cols[i] = [k]
            filledCols.appendleft(i)
            k -= 1
    filled23Cols = deque()
    #handle 2s and 3s
    for i in range(n - 1, -1, -1):
        if a[i] == 2:
            if len(filledCols) == 0 or filledCols[-1] < i:
                print('-1')
                return
            cols[i] = [cols[filledCols.pop()][0]]
            filled23Cols.append(i)
        elif a[i] == 3:
            if (len(filledCols) == 0 or filledCols[-1] < i) and len(filled23Cols) == 0:
                print('-1')
                return
            cols[i] = [k]
            if len(filled23Cols) > 0:
                cols[filled23Cols.pop()].append(k)
            else:
                cols[filledCols.pop()].append(k)
            filled23Cols.append(i)
            k -= 1
    #output
    tot=0
    for i in cols:
        tot += len(i)
    print(tot)
    for i in range(len(cols)):
        if len(cols[i]) > 0:
            for j in cols[i]:
                print(j + 1, i + 1)

def E():
    def f(orig, div):
        return (div - (orig % div)) * (orig//div)**2 + (orig % div) * (orig//div + 1)**2
 
    
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    from math import ceil
    avgSize = sum(a) / k
    rem = []
    tot=0
    k -= n
    for i in a:
        tot += i ** 2
        if i > avgSize:
            rem.append(i)
    l=len(rem)
    divs = [[rem[i]**2] for i in range(l)]
    for i in range(len(rem)):
        j = 2
        while rem[i] / j >= avgSize:
            divs[i].append(f(rem[i],j))
            j += 1
        divs[i].append(f(rem[i],j))
    #print(str(divs))
    x=[]
    for i in divs:
        for j in range(1, len(i)):
            x.append(abs(i[j] - i[j - 1]))
    x.sort(reverse=True)
    #print(str(x))
    #print(tot)
 
    print(tot - sum(x[0:k]))
            
    
E()


#check if whole thing is cycle first
#check nonreturnables: <<, <->, >>

# <-<
