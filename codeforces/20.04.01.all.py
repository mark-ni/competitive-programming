from math import sqrt
def A():
    print("NO")
def B():
    a=int(input())
    factors=[]
    for i in range(2,int(sqrt(a)) + 1):
        if a % i == 0:
            factors.append(i)
            factors.append(a//i)
    print(''.join([str(x) for x in sorted(factors)]))
def D():
    a=input()
    print(int(a[-1])%2)
C()



