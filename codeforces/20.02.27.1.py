from sys import stdin
input=stdin.readline

for _ in range(int(input())):
    n,s,k=map(int,input().split())
    k -= 1
    basicStepsUp = k//2
    basicStepsDown = basicStepsUp
    if s + basicStepsUp + 1 > n:
        basicStepsDown += n - basicStepsUp - s - 1
    elif s - basicStepsDown - 1 < 1:
        basicStepsUp += 2 + basicStepsDown - s
    print(max(basicStepsUp,basicStepsDown) +  1)




#1 2 3 4 5 6 7 8 9 10
