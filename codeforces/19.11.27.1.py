n = int(input())

def getAns(arr):
    c = arr[0]
    s = arr[1]
    
    if (s > c):
        #c=10, s=29
        baseCost = s//c #1 
        highCost = baseCost + 1 #2
        total = (s - (baseCost * c)) * highCost**2 #8
        total += (c - (s % c)) * baseCost**2
        print(str(total))
    else:
        print(s)


for i in range(n):
    getAns([int(x) for x in input().split(' ')])