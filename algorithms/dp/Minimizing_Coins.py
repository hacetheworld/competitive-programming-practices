# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------
# sys.setrecursionlimit(1000000)


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------------- SOLUTION FUNCTION ------------------


# def minCoin(arr, n, x, sm, res, i):
#     if i >= n or sm > x:
#         return float("inf")
#     if sm == x:
#         return res
#     ans = float("inf")
#     for coin in arr:
#         ans = min([ans, minCoin(arr, n, x, sm+coin, res+1, i),
#                    minCoin(arr, n, x, sm, res, i+1)])
#     return ans


def Solution(arr, n, x):
    # Write Your Code Here
    dp = [float("inf") for _ in range(x+1)]
    dp[0] = 0
    arr = sorted(arr)
    for sm in range(1, x+1):
        for coin in arr:
            if coin > sm:
                break
            dp[sm] = min(dp[sm], dp[sm-coin]+1)
    if dp[-1] == float("inf"):
        print(-1)
    else:
        print(dp[-1])


def main():
    # Take input Here and Call solution function
    n, x = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, x)


# calling main Function
if __name__ == '__main__':
    main()
