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


def helper(arr, n, i, j, dp):
    if i >= n or j < 0 or i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    left = arr[i]+min(helper(arr, n, i+2, j, dp), helper(arr, n, i+1, j-1, dp))
    right = arr[j]+min(helper(arr, n, i, j-2, dp),
                       helper(arr, n, i+1, j-1, dp))
    ans = max(left, right)
    dp[i][j] = ans
    return ans


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = get_ints_in_list()
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    helper(arr, n, 0, n-1, dp)
    # print(dp)
    print(dp[0][n-1]-(sum(arr)-dp[0][n-1]))


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
