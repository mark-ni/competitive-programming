"""
ID: markni11
LANG: PYTHON3
TASK: wormhole
"""
fin = open('wormhole.in', 'r')
fout = open('wormhole.out', 'w')
input = fin.readline

n = int(input())
l = [0] * n * 2
for i in range(n):
    l[2 * i], l[2 * i + 1] = map(int,input().rstrip().split(' '))
#print(*l)

ins = [0] * n
outs = [0] * n

def isSol(pairs):
    for i in range(0, n, 2):
        ins[pairs[i]] = pairs[i+1]
        ins[pairs[i+1]] = pairs[i]
    for i in range(n):
        pt = [l[2*i + 1], l[2 * i]]
        closest = -1
        currOut = -1
        for j in range(0, n):
            if l[2*j + 1] == pt[0]:
                if l[2*j] - pt[1] > 0:
                    if l[2*j] - pt[1] < closest or closest < 0:
                        currOut = j
                        closest = l[2*j] - pt[1]
        outs[i] = currOut
    #print(*pairs)
    #print(*ins)
    #print(*outs)
    #print()
    for i in range(n):
        start = i
        curr = outs[ins[start]]
        while True:
            if curr == -1:
                break
            elif curr == start:
                return 1
            curr = outs[ins[curr]]

def p(n):
    if (n==2):
        yield [0, 1]
    else:
        Sn_2 = p(n-2) 
        for s in Sn_2:
            yield( s + [n-2,n-1] )
            for i in range(0, (n - 1)//2):
                sn = list(s)
                sn.remove(s[2*i])
                sn.remove(s[2*i + 1])
                yield( sn + [s[2*i],  n-2, s[2*i + 1], n-1] )
                yield( sn + [s[2*i + 1], n-2, s[2 * i], n-1] )

tot = 0
for i in p(n):
    if isSol(i):
        tot += 1

fout.write(str(tot) + "\n")
fout.close()
