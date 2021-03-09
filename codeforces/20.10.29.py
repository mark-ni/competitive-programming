from sys import stdin
input=stdin.readline

def A():
    t=int(input())
    for __ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=a[::-1]
        for i in range(n//2):
            b[i] *= -1
        print(*b)

def B():
    t=int(input())
    for __ in range(t):
        n,m=map(int,input().split())
        firstCol=[0]*n
        scrambledRows=[0 for i in range(n)]
        scrambledCols=[0 for i in range(m)]
        fixed=[0 for i in range(n)]
        for i in range(n):
            scrambledRows[i]=list(map(int,input().split()))
        for i in range(m):
            scrambledCols[i]=list(map(int,input().split()))
        char=scrambledRows[0][0]
        for i in range(m):
            if char in scrambledCols[i]:
                firstCol=scrambledCols[i].copy()
                break
        for i in range(n):
            for j in scrambledRows:
                if j[0]==firstCol[i]:
                    break
            fixed[i]=j
        for i in fixed:
            print(*i)

def C():
    a=sorted(list(map(int,input().split())))
    n=int(input())
    b=sorted(list(map(int,input().split())))
    starts=[0]*6
    # assumptions made
    # - if u are on a higher string, u will never go down a string
    # - you can greedily decide when to move up a string
    for i in range(6):
        # j = current string number
        j=i
        # starting low is the first difference. The low only changes
        # when you change strings
        low=b[0]-a[i]
        # if the last note on string 5 is higher than the first note
        # the high will be at least that b[-1] - a[5]
        high=max(low, b[-1]-a[5])
        # k = current note
        k=1
        while k < n:
            # if you can go up a string without changing the low,
            # then do it. This also means when diff > high, the
            # next string up will always make you dip below low.
            while j < 5 and b[k]-a[j+1] >= low:
                j += 1
            diff=b[k]-a[j]
            if j < 5:
                # if you are about to widen the bounds, greedily
                # decide whether going up a string or accepting a
                # higher high is better (PROBABLE SOURCE OF ERROR)
                if diff > high:
                    diffUp=b[k]-a[j+1]
                    if low - diffUp <= diff - high:
                        j += 1
                        low = diffUp
                    else:
                        high = diff
            else:
                if diff > high:
                    high = diff
            k+=1
        #store range for each starting string
        starts[i]=high-low
    print(min(starts))

def D():
    t=int(input())
    for __ in range(t):
        _=0
C()
