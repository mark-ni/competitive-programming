from sys import stdin
input = stdin.readline

#def getAns(li1, li2, n, m):
#    l1 = [0] * m
#    l2 = [0] * m
#    for i in range(n):
#        l1[li1[i]] += 1
#        l2[li2[i]] += 1
#    for i in range(m):
#        if l1[i:] + l1[:i] == l2:
#            return m - i

def getAns(li1, li2, n, m):
    d1 = [0] * (n - 1)
    d2 = [0] * (n - 1)
    li1.sort()
    li2.sort()
    for i in range(n - 1):
        d1[i] = li1[i + 1] - li1[i]
        d2[i] = li2[i + 1] - li2[i]
    for i in range(n - 1):
        if d1[i:] == d2[0:n-i-1]:
            if d1[0:i-1] == d2[n-i:]:
                return n - i
string = '''30 20
13 4 5 0 18 3 13 1 2 6 17 10 1 17 2 12 16 8 10 1 15 19 19 3 17 19 8 11 2 5
5 13 1 11 0 10 16 18 9 6 2 15 2 6 4 8 3 10 18 4 6 17 7 7 7 2 15 13 4 8'''
#def getAns(li1, li2, n, m):
#    li1.sort()
#    li2.sort()
#    for i in range(m):
#        if li1 == li2:
#            return i
#        else:
#            for j in range(n):
#                li1[j] += 1
#                if li1[j] >= m:
#                    li1[j] %= m
#            li1.sort()
#    return -1

k = [int(x) for x in input().split(' ')]
n = k[0]
m = k[1]
print(getAns(list(map(int, input().split(' '))),
       list(map(int, input().split(' '))), n, m))
