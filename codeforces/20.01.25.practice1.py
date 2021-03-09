from sys import stdin,stdout
input = stdin.readline

def getAns(s):
    s = s.rstrip().split('.')
    l = len(s)
    if len(s[0]) < 1 or len(s[0]) > 8:
        stdout.write("NO")
        return
    for i in range(1,l-1):
        if len(s[i]) < 2 or len(s[i]) > 11:
            stdout.write("NO")
            return
    if (len(s[l-1]) < 1 or len(s[l-1]) > 3):
        stdout.write("NO")
        return
    stdout.write("YES")
    leftOffAt = 0
    for i in range(0, l - 1):
        stdout.write('\n')
        stdout.write(s[i][leftOffAt:])
        stdout.write('.')
        k = (len(s[i + 1]) // 9) * (len(s[i+1]) % 9) + 1
        stdout.write(s[i+1][0:k])
        leftOffAt = k
    stdout.write(s[l - 1][leftOffAt:])
    return

getAns(input())
    
