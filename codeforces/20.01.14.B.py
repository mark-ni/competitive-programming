import math
for _ in range(int(input())):
    A,B=map(int,input().split(' '))
    print(math.floor(math.log10(B+1))*A)
