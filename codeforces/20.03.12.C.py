from sys import stdin
input=stdin.readline

def getAns(s):
    largestGap = 0
    lastR = 0
    for i in range(1,len(s)):
        if s[i] == 'R':
            if i - lastR > largestGap:
                largestGap = i - lastR
            lastR = i
    print(largestGap)
    
n=int(input())
for _ in range(n):
    getAns('R' + input().rstrip() + 'R')
