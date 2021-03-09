n = int(input())
for i in range(n):
    h,m=map(int,input().split(' '))
    minutes = 0
    print(((23 - h))*60 + ((60-m)))
    
