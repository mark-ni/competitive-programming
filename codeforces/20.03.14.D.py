from math import floor, log

def getAns(u,v):
    if u > v or u % 2 != v % 2:
        print(-1)
        return
    if u == 0 and v == 0:
        print(0)
        return
    pw=floor(log(
    

u,v=map(int,input().split()))
getAns(u,v)
