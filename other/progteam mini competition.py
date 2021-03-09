from sys import stdin
input=stdin.readline

def A():
    #WORMHOLES
    n=int(input())
    wormholes=[]
    pairs=[0]*(12*11*9*7*5*3)
    pInd=0
    for i in range(n):
        wormholes.append(list(map(int,input().split())))

    def getPairs(pair, currSet, x, i):
        if len(currSet) == 1:
            pair[x] = currSet.pop()
            pair[pair[x]] = x

            for i in range(12):
                p[pInd*12 + i] = pair[i]
            pInd += 1
        else:
            x=min(currSet)
            currSet.remove(x)
            for k in currSet:
                getPairs(pair, currSet, x, k)

    #set11=set(range(12))
    #for second in range(1, 12):
    #    pair0=[0,second]
    #    set9=set11.copy()
    #    set9.remove(second)
    #    third=min(set9)
    #    set9.remove(third)
    #    for fourth in set9:
    #        pair1=[third,fourth]
    #        set7=set9.copy()
    #        set7.remove(fourth)
    #        fifth=min(set7)
    #        set7.remove(fifth)
    #        for sixth in set7:

def B():
    #FIND THE GRAPH
    from sys import stdout
    n=int(input())
    table=[[0 for j in range(n)] for i in range(n)]
    connects=[0]*n
    for i in range(n):
        print("? 1",i+1)
        stdout.flush()
        connects[i] = int(input())
    for i in range(n):
        for j in range(i + 1, n):
            print("? 2", i + 1, j + 1)
            stdout.flush()
            x=int(input())
            if x != connects[i] + connects[j]:
                table[i][j] = 1
                table[j][i] = 1
    print("!")
    for row in table:
        print(*row)
B()
    

