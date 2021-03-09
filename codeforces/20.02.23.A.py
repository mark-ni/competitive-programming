from sys import stdin
input=stdin.readline
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    top = (y)*(a)
    bottom=(b-y-1)*a
    right=(a-x-1)*b
    left=(x)*(b)
    print(max([top,bottom,left,right]))
                                          
