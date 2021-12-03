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


def Solution(n, m, k):
    # Write Your Code Here
    score = 0
    mod = pow(10, 9)+9
    lft = n-m
    tmpAns = 0
    while m > 0:
        if lft:
            m -= (k-1)
            lft -= 1
            tmpAns = (tmpAns+(k-1)) % mod
        else:
            t = min(m, k)
            score = (score + t) % mod
            if m-k >= 0:
                score = (2*score) % mod
            m -= (t)
    score = ((score % mod)+(tmpAns % mod)) % mod
    print(score)


def main():
    # Take input Here and Call solution function
    n, m, k = get_ints_in_variables()
    Solution(n, m, k)


# calling main Function
if __name__ == '__main__':
    main()
