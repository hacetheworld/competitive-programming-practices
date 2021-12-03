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


def Solution(n, k, d):
    # Write Your Code Here
    if n > pow(k, d):
        print(-1)
        return
    t = 1
    a = 1
    for _ in range(d):
        i = 0
        while i < n:
            for _ in range(t):
                print(a, end=" ")
                i += 1
                if i == n:
                    break
            a += 1
            if a > k:
                a = 1
        print()
        a = 1
        t *= k


def main():
    # Take input Here and Call solution function
    n, k, d = get_ints_in_variables()
    Solution(n, k, d)


# calling main Function
if __name__ == '__main__':
    main()
