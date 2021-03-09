import math
m = int(input())

def getAns(n):
    k = math.floor(math.sqrt(n))
    string = "0"
    for i in range(1, k + 1):
        string += " " + str(i)
    total = k
    
    if (k == n//k):
        k -= 1
    
    for i in range(k, 0, -1):
        string += " " + str(n//i)
    
    total += k + 1
    
    print(total)
    print(string)
    
    

for i in range(m):
    getAns(int(input()))