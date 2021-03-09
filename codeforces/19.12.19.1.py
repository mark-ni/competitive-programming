from sys import stdin
input = stdin.readline

def getAns(p, h):
    lp = [0] * 26
    for i in p:
        lp[i] += 1
    for i in range(0, len(h) - len(p) + 1):
        lh = [0] * 26
        for j in range(i, i + len(p)):
            lh[h[j]] += 1
        if lh == lp:
            return True
    return False

n = int(input())

for i in range(n):
    p = [ord(i) - ord('a') for i in input().rstrip()]
    h = [ord(i) - ord('a') for i in input().rstrip()]
    if getAns(p, h):
        print("YES")
    else:
        print("NO")
        

    
