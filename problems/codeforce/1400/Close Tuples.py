from bisect import *
from sys import *
input = stdin.readline
for _ in range(int(input())):
    n = int(input())
    l = sorted(list(map(int, input().split())))
    c = 0
    for i in range(n):
        b = bisect_right(l, l[i]+2)-1
        c += ((b-i)*(b-i-1)//2)
    print(c)
