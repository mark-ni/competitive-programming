t=int(input())
def getAns():
    n=int(input())
    a=[False]*60*24
    b=[False]*60*24
    k=0
    string=['']*n
    slots=[() for i in range(n)]
    for i in range(n):
        s,e=map(int,input().split())
        slots[i] = (s,e)
    slots2=sorted(slots)
    #print(str(slots))
    #print(str(slots2))
    for s,e in slots2:
        i=slots.index((s,e))
        if True in a[s:e]:
            if True in b[s:e]:
                return 'IMPOSSIBLE'
            else:
                if string[i] != '':
                    i = slots.index((s,e), i+1)
                string[i]='J'
                for j in range(s,e):
                    b[j] = True
        else:
            if string[i] != '':
                i = slots.index((s,e), i+1)
            string[i]='C'
            for j in range(s,e):
                a[j] = True
    return ''.join(string)

for _ in range(t):
    s=getAns()
    print('Case #' + str(_ + 1) + ':', s)
