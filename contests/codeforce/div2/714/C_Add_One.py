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


def Solution(dp, mod):
    # Write Your Code Here

    for _ in range(get_int()):
        n, m = get_ints_in_variables()
        n = str(n)
        ans = 0
        for c in n:
            ans += (dp[m][int(c)]) % mod
        print(ans)


def main():
    # Take input Here and Call solution function
    mod = pow(10, 9)+7

    dp = [[0 for _ in range(10)] for _ in range(200005)]
    for i in range(10):
        dp[0][i] = 1

    for i in range(1, 200005):
        for j in range(9):
            # print(i, j)
            dp[i][j] = dp[i - 1][j + 1] % mod
        dp[i][9] = ((dp[i - 1][1] % mod) + (dp[i - 1][0] % mod)) % mod
    Solution(dp, mod)


# calling main Function
if __name__ == '__main__':
    main()
