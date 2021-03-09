from sys import stdin
input = stdin.readline

def f(x,y):
    return (x|y) - y

n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)

01011
00110
00100
00000

1st
01111 -> 01001
01101 -> 01000
01000 -> 01000

