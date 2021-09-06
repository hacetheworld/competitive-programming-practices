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


def helper(arr, n, k, i, dp):
    if k == 1:
        return arr[i]-arr[0]
    if i <= 0 or k <= 0:
        return float("inf")
    # print(k, i, "jjjj")
    if dp[i][k] != float("inf"):
        return dp[i][k]
    tmpAns = 0
    for l in range(i, k-2, -1):
        tmpAns = (arr[i]-arr[l])
        tmpAns += helper(arr, n, k-1, l-1, dp)
        dp[l][k] = tmpAns
    return dp[i][k]


def Solution(arr, n, k):
    # Write Your Code Here
    dp = []
    for i in range(1, n):
        dp.append(arr[i-1]-arr[i])
    dp = sorted(dp)
    ans = arr[-1]-arr[0]
    for i in range(k-1):
        ans += dp[i]
    print(ans)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
