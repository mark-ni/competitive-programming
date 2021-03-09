from sys import stdin
input=stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    rows=[set() for i in range(n)]
    cols=[set() for i in range(n)]
    trace=0
    for row in range(n):
        r=list(map(int,input().split()))
        trace+=r[row]
        rows[row] = set(r)
        for col in range(n):
            cols[col].add(r[col])
    rr=sum([int(len(rows[x]) < n) for x in range(n)])
    rc=sum([int(len(cols[x]) < n) for x in range(n)])
    print('Case #' + str(_+1) + ': ', trace, rr, rc)
