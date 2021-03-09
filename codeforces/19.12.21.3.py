from sys import stdin, stdout

n, k = map(int, input().split(' '))
x = input()

def getAns(n, k, x):
    xi = int(x)
    pref = x[0:k]
    newnum = ""
    while newnum < x:
        newnum = pref * (n//k)
        newnum += pref[:n%k]
        if len(newnum) > len(x) or newnum >= x:
            stdout.write(str(len(newnum)) + "\n")
            stdout.write(str(newnum))
            return
        pref = str(int(pref) + 1)

getAns(n, k, x)






