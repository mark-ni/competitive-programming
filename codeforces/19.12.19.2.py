#from sys import stdin
#input = stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split(' '))
    d = abs(a - b)
    if d == 0:
        print(0)
    else:
        for i in range(4 - (d % 2) * 2, 10**5, 4):
            if i * (i + 1)//2 >= d:
                if i * (i - 1)//2 >= d:
                    print(i - 1)
                else:
                    print(i)
                break

    
        

    
