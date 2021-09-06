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


def helper(n, c, k, d, dp, mod):
    if n < 0:
        return 0
    if n == 0:
        if c >= d:
            return 1
        return 0
    if dp[n][c] != -1:
        return dp[n][c]
    tmp = 0
    for i in range(1, k+1):
        tmp += (helper(n-i, max(c, i), k, d, dp, mod))
        tmp = tmp % mod
    dp[n][c] = tmp
    return tmp


def Solution(n, k, d):
    # Write Your Code Here
    mod = pow(10, 9)+7
    dp = [[-1 for _ in range(101)] for _ in range(101)]
    ans = helper(n, 0, k, d, dp, mod)
    print(ans)


def main():
    # Take input Here and Call solution function
    n, k, d = get_ints_in_variables()
    Solution(n, k, d)


# calling main Function
if __name__ == '__main__':
    main()
