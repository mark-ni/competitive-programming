from sys import stdin
input = stdin.readline

def getAns(s):
    if '1' in s:
        firstIndex = s.index('1')
        lastIndex = firstIndex
        for i in range(firstIndex + 1, len(s)):
            if s[i] == '1':
                lastIndex = i
        count = 0
        for i in range(firstIndex, lastIndex):
            if s[i] == '0':
                count += 1
        return count
    else:
        return 0

for _ in range(int(input())):
    print(getAns(input()))
    
    
    
