from sys import stdin
def getAns(n,s):
    zcount=0
    ocount=0
    for i in s:
        if i == 0: ocount += 1
        else: zcount += 1
    if ocount != zcount:
        print(-1)
        return
    

n=int(input())
s=[ord(x) - 40 for x in input().rstrip()]
getAns(n,s)
