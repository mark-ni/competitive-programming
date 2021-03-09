from sys import stdin
from collections import deque

input = stdin.readline

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def getAns(s):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dictionary = [''] * 52
    for i in range(1, len(s)):
        j = (ord(s[i - 1]) - 97)*2
        if s[i] != dictionary[j] and s[i] != dictionary[j+1]:
            if dictionary[j] == '':
                dictionary[j] = s[i]
            elif dictionary[j+1] == '':
                dictionary[j+1] = s[i]
            else:
                print("NO")
                return
        k = (ord(s[i]) - 97)*2
        if s[i - 1] != dictionary[k] and s[i - 1] != dictionary[k+1]:
            if dictionary[k] == '':
                dictionary[k] = s[i - 1]
            elif dictionary[k+1] == '':
                dictionary[k+1] = s[i - 1]
            else:
                print("NO")
                return
    if len(s) == 1:
        print("YES")
        print("abcdefghijklmnopqrstuvwxyz")
        return
    startInd = 0
    keyboard = ''
    for i in range(52):
        if dictionary[i] != '':
            startInd = i
            keyboard = alphabet[i//2]
            break
    print('YES')
    nextLetter = 2*alphabet.index(i)
    keyboard += dictionary[nextLetter]
    while dictionary[nextLetter] != '' or dictionary[nextLetter+1] != ''):
        
        
    
for _ in range(int(input())):
    getAns(input().rstrip())
