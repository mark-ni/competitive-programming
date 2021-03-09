from sys import stdin,stdout
input=stdin.readline
def conv2(l1, l2):
    if l1 == l2:
        return l1
    if l1 == 'S':
        if l2 == 'E':
            return 'T'
        return 'E'
    if l1 == 'E':
        if l2 == 'S':
            return 'T'
        return 'S'
    if l1 == 'T':
        if l2 == 'E':
            return 'S'
        return 'E'

n,k=map(int,input().split())
sets = ['']*n
g={}
tot = 0
for i in range(n):
    sets[i] = input().rstrip()
    if g.get(sets[i],0) > 0:
        tot += g[sets[i]]
    for j in range(0, i):
        string=''.join([conv2(sets[i][m],sets[j][m]) for m in range(k)])
        g[string]=g.get(string,0) + 1
stdout.write(str(tot))
            
