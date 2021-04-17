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

# -------------- SOLUTION FUNCTION ------------------


# def helper(n, k, dp, N, p):
#     if n == 0 or k <= 1:
#         return 1

#     if dp[n][k] != -1:
#         return dp[n][k]
#     dp[n][k] = ((helper(n-1, k, dp, N, p) % p) +
#                 (helper(N-n, k-1, dp, N, p) % p)) % p
#     return dp[n][k]


def Solution(n, k):
    # Write Your Code Here

    N, K = n, k
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    mod = int(1e9+7)
    for k in range(2, K+1):
        for n in range(1, N+1):
            dp[n][k] = (1 + dp[N-n][k-1] + dp[n-1][k]) % mod
    print((1+dp[N][K]) % mod)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        Solution(n, k)


# calling main Function
if __name__ == '__main__':
    main()
