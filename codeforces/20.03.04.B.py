from sys import stdin
input=stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    e=n%2
    s=input().rstrip()
    k=1
    smallest=s
    for i in range(1,n):
        if (e + i) % 2 == 0:
            if s[i:n] + s[:i] < smallest:
                smallest = s[i:n] + s[:i]
                #print('1: ' + str(smallest))
                k=i+1
        else:
            if s[i:n] + s[i-1::-1] < smallest:
                smallest=s[i:n] + s[i-1::-1]
                #print('2: ' + str(smallest))

                k=i+1
    print(smallest)
    print(k)
