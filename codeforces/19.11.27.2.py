n = int(input())

def getAns(arr):
    a = arr[0]
    b = arr[1]
    
    if (b > 2 * a):
        print("NO")
    elif (a > 2 * b):
        print("NO")
    else:
        if (2*a - b) % 3 == 0:
            print("YES")
        else:
            print("NO")

for i in range(n):
    getAns([int(x) for x in input().split(' ')])