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


def Solution(n, m):
    # Write Your Code Here

    needm = n//2 - 1 if n % 2 == 0 else n//2
    if m < needm or m >= n:
        print(-1)
        return
    res = [1 for _ in range(n+m)]
    i = 4
    t = n+m
    while i < t-2 and m > 0:
        res[i-1] = 0
        m -= 1
        i += 4
    i = 2
    print(res, "snjds")
    while i < t and m > 0:
        res[i-1] = 0
        m -= 1
        i += 4

    for v in res:
        print(v, end="")
    print()


def main():
    # Take input Here and Call solution function
    n, m = get_ints_in_variables()
    Solution(m, n)


# calling main Function
if __name__ == '__main__':
    main()
