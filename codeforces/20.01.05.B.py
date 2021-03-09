from sys import stdin
input = stdin.readline
n,k=map(int,input().split(' '))
st = [[]]*n
for i in range(n):
    st[i] = list(input())

tot = 0
diff = True
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            for d in range(k):
                truths = 0
                if st[a][d] == st[b][d]: truths += 1
                if st[b][d] == st[c][d]: truths += 1
                if truths == 2:
                    tot += 1
                    f = False
                    break
                if st[a][d] == st[c][d]: truths += 1
                if truths > 0: f = False
            if f: tot += 1
print(tot)
