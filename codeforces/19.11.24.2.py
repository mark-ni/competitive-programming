n = int(input())

def getAns(k):
    li = [int(x) for x in input().split(' ')]

    indicesavail = list(range(1, li[0]))
    indiceslength = len(indicesavail)
    
    e = 0
    f = 0

    string = str(li[0])

    for i in range(1, len(li)):
        e = li[i]
        f = li[i - 1]
        if e == f:
            if len(indicesavail) == 0:
                print(-1)
                return
            string += " " + str(indicesavail[0])
            indicesavail.pop(0)
        else:
            string += " " + str(e)
            indicesavail.extend(list(range(f+1,e)))
    print(string)
    return
    
        
for i in range(n):
    getAns(int(input()))