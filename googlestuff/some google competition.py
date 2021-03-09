#GENERATE TEST CASES
import random

def genRandSeq(n, m):
    li = [0] * n
    for i in range(n):
        li[i] = random.randrange(m)
    return li

def genRandomPermut(lim):
    li = [0] * lim
    for i in range(1, lim + 1):
        li[i - 1] = i
    return li

def genRandSeq1269(lim, li, m):
    ans = random.randrange(m)
    l = [0] * lim
    for i in range(lim):
        l[i] = (li[i] + ans) % m
    random.shuffle(l)
    return l
