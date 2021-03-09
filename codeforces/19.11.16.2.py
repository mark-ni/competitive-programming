def getAns():
    n = int(input())

    a = set([])
    b = [int(x) for x in input().split(' ')]
    c = set([])
    days = []
    
    for e in b:
        if e > 0:
            if e not in a:
                if e in c:
                    if len(a) == 0:
                        days.append(len(c) * 2)
                        c = set([])
                    else:
                        print(-1)
                        return
                a.add(e)
                c.add(e)
            else:
                print(-1)
                return
        else:
            if -1 * e in a:
                a.remove(-1 * e)
            else:
                print(-1)
                return
    if len(a) > 0:
        print(-1)
        return
    
    days.append(len(c) * 2)
    c = set([])
    
    print(len(days))
    string = str(days[0])
    for i in range(1, len(days)):
        string += ' ' + str(days[i])
    print(string)
    return

getAns()
    
                
