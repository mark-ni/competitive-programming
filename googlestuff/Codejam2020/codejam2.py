from sys import stdin
input=stdin.readline

t=int(input())
for _ in range(t):
    s=[int(x) for x in input().rstrip()]
    string='(' * s[0] + str(s[0])
    i=0
    for i in range(1, len(s)):
        if s[i - 1] < s[i]:
            string += '(' * (s[i] - s[i - 1])
        elif s[i - 1] > s[i]:
            string += ')' * (s[i - 1] - s[i])
        string += str(s[i])
    string += ')' * s[len(s) - 1]
    print('Case #' + str(_) + ':', string)
    
    
