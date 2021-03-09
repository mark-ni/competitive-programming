from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        if sum(a) == 0:
            print("NO")
        elif sum(a) > 0:
            a.sort(reverse=True)
            print("YES")
            print(*a)
        else:
            a.sort()
            print("YES")
            print(*a)

def B():
    from collections import deque
    t=int(input())
    for _ in range(t):
        n,k=map(int,input().split())
        s=[bool(ord(x) - ord('L')) for x in input().rstrip()]

        lastGame = False
        score = 0
        for i in range(n):
            if s[i]:
                if lastGame:
                    score += 2
                else:
                    score += 1
                lastGame=True
            else:
                lastGame=False

        startW=0
        endW=n-1
        while startW < n and not s[startW]:
            startW += 1
        while endW >= 0 and not s[endW]:
            endW -= 1
        streak=0
        wlws=deque()
        for i in range(startW+1, endW+1):
            if s[i] and streak > 0:
                wlws.append(streak)
                streak=0
            elif not s[i]:
                streak += 1
        
        wlws=sorted(list(wlws))

        j = 0
        while j < len(wlws) and k >= wlws[j]:
            score += (2 * wlws[j] + 1)
            k -= wlws[j]
            j += 1
            
        if k > 0:
            remainingLs = startW + (n - 1 - endW)
            if startW == n:
                remainingLs = n
                score -= 1
            if j < len(wlws):
                remainingLs = wlws[j]
            score += min(remainingLs, k) * 2
        print(score)
        

def C():
    r,n=map(int,input().split())
    xs=[0]*n
    ys=[0]*n
    ts=[0]*n
    tots=[0]*n
    for i in range(n):
        ts[i],xs[i],ys[i]=map(int,input().split())
    for i in range(n - 1, -1, -1):
        j = i + 1
        while j < n and ts[j]-ts[i] <= 4*r:
            if abs(xs[j]-xs[i])+abs(ys[j]-ys[i]) <= ts[j]-ts[i]:
                tots[i] = max(tots[j], tots[i])
            j += 1
        if xs[i]-1 + ys[i]-1 <= ts[i]:
            tots[i] += 1
        else:
            tots[i]=0
    print(max(tots))

def newC():
    r,n=map(int,input().split())
    xs=[0]*n
    ys=[0]*n
    ts=[0]*n
    tots=[0]*n
    runningMax=0
    runningMaxInd=0
    for i in range(n):
        ts[i],xs[i],ys[i]=map(int,input().split())
    for i in range(n):
        j = i - 1
        while j >= 0 and ts[i]-ts[j] <= 4*r:
            if abs(xs[j]-xs[i])+abs(ys[j]-ys[i]) <= ts[i]-ts[j]:
                tots[i] = max(tots[j], tots[i])
            j -= 1
        if xs[i]-1 + ys[i]-1 <= ts[i]:
            tots[i] += 1
        else:
            tots[i]=0
    print(max(tots))
        

def D():        
    n=int(input())
    c=list(map(int,input().split()))

    def transform(parts,c):
        h=[]
        i=0
        for part in parts:
            h.append(c[i:i+part])
            i += part
        c.clear()
        for j in range(len(h) - 1, -1, -1):
            c += h[j]
        return c

    if c == [1] or c == sorted(c):
        print(0)
        return
    transforms=[[] for i in range(52)]
    targetInd=c.index(1)
    if targetInd != 0:
        transforms[0]=[2,targetInd,n-targetInd]
        c=transform([targetInd,n-targetInd],c)
        transIndex=1
    else:
        transIndex=0
    currTrans=[]

    numSorted=1
    targetNum=2
    inverted=False
    
    while c != sorted(c):
        if not inverted:
            k=c.index(targetNum) + 1 - numSorted
            leftOver=n - numSorted - k
            if leftOver != 0:
                currTrans = ([1]*numSorted) + [k] + [leftOver]
            else:
                currTrans = ([1]*numSorted) + [k]
        else:
            k=n - numSorted - c.index(targetNum)
            leftOver=n - numSorted - k
            if leftOver != 0:
                currTrans = [leftOver] + [k] + ([1]*numSorted)
            else:
                currTrans = [k] + ([1]*numSorted)
        c=transform(currTrans,c)
        numSorted += 1
        targetNum += 1
        inverted = not inverted
        transforms[transIndex] = [len(currTrans)] + currTrans
        transIndex += 1

    print(transIndex)
    for i in range(transIndex):
        print(*transforms[i])        
    
newC()
