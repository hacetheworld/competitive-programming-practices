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


def slimes(arr, i, j, dp, sums):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    minCoast = float("inf")
    for k in range(i, j):
        minCoast = min(minCoast, slimes(arr, i, k, dp, sums) +
                       slimes(arr, k+1, j, dp, sums)+sums[i][j])
    dp[i][j] = minCoast
    return minCoast


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    sums = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if i == j:
                sums[i][j] = arr[j]
            else:
                sums[i][j] = arr[j]+sums[i][j-1]
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    print(slimes(arr, 0, n-1, dp, sums))


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
