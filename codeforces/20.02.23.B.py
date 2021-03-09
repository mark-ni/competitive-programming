from sys import stdin
input=stdin.readline
t=int(input())
for _ in range(t):
    a,b,p=map(int,input().split())
    s=[ord(x) - ord('A') for x in input().rstrip()]
    l = len(s)
    k = [a,b]
    m = [0,0]
    currChar = s[l - 2]
    while p >= k[currChar]:
        p -= k[currChar]
        m[currChar] += 1
        currChar = (currChar + 1) % 2
    m = sum(m)
    currChar = s[l - 2]
    if m == 0:
        print(l)
    else:
        for i in range(l - 2, -1, -1):
            if currChar == s[i]:
                if (i == 0):
                    currIndex = 1
                    break
                continue
            else:
                m -= 1
                #print(str(i) + ": " +str(m) + str(",") + str(currChar))
                if m <= 0:
                    currIndex = i + 2
                    break
                elif i == 0:
                    currIndex = 1
                    break
                currChar = s[i]
        print(currIndex)
    
        
