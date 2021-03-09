from sys import stdin
from collections import deque

input = stdin.readline

def getAns(s):
    keyboard = deque()
    keyboard.appendleft(s[0])
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet.remove(s[0])
    for i in range(1,len(s)):
        if s[i] not in keyboard:
            if keyboard.index(s[i - 1]) == 0:
                keyboard.appendleft(s[i])
            elif keyboard.index(s[i - 1]) == len(keyboard) - 1:
                keyboard.append(s[i])
            else:
                print("NO")
                return
            alphabet.remove(s[i])
        else:
            if abs(keyboard.index(s[i]) - keyboard.index(s[i - 1])) > 1:
                print("NO")
                return
    print("YES")
    print(''.join(keyboard) + ''.join(alphabet))

for _ in range(int(input())):
    getAns(list(input().rstrip()))
