# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def Solution(n, l, r, s):
    # Write Your Code Here
    permutaion = [0 for _ in range(n)]
    p = 1
    leftSum = 0
    for i in range(l, r+1):
        leftSum += p
        p += 1
    pl = p-1
    p = n
    right = 0
    for i in range(l, r+1):
        right += p
        p -= 1
    if s < leftSum or s > right:
        print(-1)
        return

    hm = {}
    p = n
    for i in range(l-1, r):
        while s-p < leftSum-pl:
            p -= 1
        hm[p] = True
        s -= p
        leftSum -= pl
        permutaion[i] = p
        p -= 1
        pl -= 1
    p = 1
    for i in range(l-1):
        while p in hm:
            p += 1
        permutaion[i] = p
        hm[p] = True
        p += 1
    p = 1
    for i in range(r, n):
        while p in hm:
            p += 1
        permutaion[i] = p
        hm[p] = True
        p += 1
    print(*permutaion)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, l, r, s = get_ints_in_variables()
        Solution(n, l, r, s)


# calling main Function
if __name__ == '__main__':
    main()
