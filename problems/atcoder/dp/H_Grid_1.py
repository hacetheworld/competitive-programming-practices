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


def gridPath(grid, dp, h, w, mod):
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if i == h-1 and j == w-1:
                continue
            if grid[i][j] == "#":
                dp[i][j] = 0
            else:
                if i != h-1:
                    dp[i][j] = (dp[i][j] % mod + dp[i+1][j] % mod) % mod
                if j != w-1:
                    dp[i][j] = (dp[i][j] % mod + dp[i][j+1] % mod) % mod


def Solution(grid, h, w):
    # Write Your Code Here
    mod = pow(10, 9)+7
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[h-1][w-1] = 1
    gridPath(grid, dp, h, w, mod)
    # print(dp)
    print(dp[0][0])


def main():
    # Take input Here and Call solution function
    h, w = get_ints_in_variables()
    grid = []
    for _ in range(h):
        grid.append([c for c in get_string()])
    Solution(grid, h, w)


# calling main Function
if __name__ == '__main__':
    main()
