from sys import stdin
input = stdin.readline

def getAns(s):
    if s < 10:
        return s
    else:
        return s + (s - 10)//9 + 1

t = int(input())
for _ in range(t):
    s = int(input())
    print(getAns(s))


#10-11, 19-21, 28-31, 
