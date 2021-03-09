from sys import stdin
#input = stdin.readline
 
m = int(input())
for i in range(m):
    n, s = map(int, input().rstrip().split(' '))
    l = list(map(int, input().rstrip().split(' ')))
    currTot = 0
    c = 0
 
    if s >= sum(l):
        print(0)
    else:
        while currTot + l[c] < s:
            currTot += l[c]
            c+=1
        currTot += l[c]
        if c < n - 1 and l[c + 1] >= max(l[0:c+1]):
            print(0)
        else:
            print(l.index(max(l[0:c+1])) + 1)
        
