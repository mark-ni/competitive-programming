#19.12.14.1.py
import sys
#input = sys.stdin.readline

n = int(input())

for i in range(n):
    string = input().split('_')[-1]
    if string[-2:] == "po":
        print("FILIPINO")
    elif string[-4:] == "desu" or string[-4:] == "masu":
        print("JAPANESE")
    else:
        print("KOREAN")