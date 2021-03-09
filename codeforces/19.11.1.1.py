#started 12:24
def computeGCD(x, y): 
   while(y): 
       x, y = y, x % y 
   return x

n = int(input())
for i in range(n):
    asdf = [int(x) for x in input().split(' ')]
    a = asdf[0]
    b = asdf[1]
    if computeGCD(a, b) > 1:
        print("Infinite")
    else:
        print("Finite")
