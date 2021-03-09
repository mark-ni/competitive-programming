n = int(input())

def getAns(li):
    for x in li:
        if x > 14:
            if x % 14 <= 6 and x % 14 > 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")



getAns([int(x) for x in input().split(' ')])
