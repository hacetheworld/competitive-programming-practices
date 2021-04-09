# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout
# sys.setrecursionlimit(1 << 10)
# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------------- SOLUTION FUNCTION ------------------


def helper(n, k, dp, N, mod):
    # if n == 0 or k <= 1:
    #     return 1
    # if dp[n][k] != -1:
    #     return dp[n][k]
    # dp[n][k] = (helper(n-1, k, dp, N, mod) %
    #             mod+helper(N-n, k-1, dp, N, mod) % mod) % mod
    # return dp[n][k]
    # print(dp)
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] % mod+dp[N-i][j-1] % mod) % mod
    return dp[n][k]


def Solution(n, k):
    # Write Your Code Here
    mod = pow(10, 9)+7
    dp = [[1 for _ in range(k+1)] for _ in range(n+1)]
    print(helper(n, k, dp, n, mod))


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()
