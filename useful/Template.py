import io, os
from collections import deque, defaultdict
import math
#from sys import stdin
#input=stdin.readline
#input=io.StringIO(os.read(0,os.fstat(0).st_size).decode()).readline
input=io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
