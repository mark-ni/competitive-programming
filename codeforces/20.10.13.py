from sys import stdin
input=stdin.readline


def p1():
    from collections import deque
    t=int(input())
    for _ in range(t):
        n=int(input())
        s=[bool(int(x)) for x in input().rstrip()]
        l=deque()
        curr=s[0]
        currLength=1
        for i in range(1, n):
            if s[i] == curr:
                currLength += 1
            else:
                l.append(currLength)
                currLength = 1
                curr = not curr
        l.append(currLength)

        j = 0
        tot = 0
        while len(l) > 0:
            while j < len(l) and l[j] == 1:
                j += 1
            
            if j < len(l):
                l[j] -= 1
            else:
                l.pop()
                j -= 1
                
            if len(l) > 0:
                l.popleft()
                if j > 0:
                    j -= 1
                
            
            tot += 1
        print(tot)

def p2():
    from collections import deque

    def binSearch(x, d, left, right):
        #nonrecursive
        while right - left >= 2:
            mid = (left + right) // 2
            if x < d[mid]: right = mid
            else: left = mid
        if right == left or x < d[left]: return left
        else: return right
#0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
#  0   1   2   3   4   5   6   7   8
    
    n=int(input())
    s=[ord(x)-ord('a') for x in input().rstrip()]
    rev=s[::-1]

    lis=[deque() for i in range(26)]
    for i in range(n):
        lis[s[i]].append(i)

    ops = 0
    ordered = []
    
    for i in range(n):
        letter=rev[i]
        origInd = lis[letter].popleft()
        indInd = binSearch(origInd, ordered, 0, len(ordered))
        numSwaps = len(ordered) - indInd
        ordered = ordered[0:indInd] + [origInd] + ordered[indInd:]
        ops += (origInd + numSwaps - i)

    print(ops)
p2()
        
        

        
    
    
