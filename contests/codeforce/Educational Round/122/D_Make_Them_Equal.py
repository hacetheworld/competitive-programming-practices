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


def helper(arr, c, i, n, k, dp, hm):
    if i >= n:
        return 0
    if dp[i][k] != -1:
        return dp[i][k]
    ans = 0
    if hm[arr[i]] <= k:
        ans = helper(arr, c, i+1, n, k-hm[arr[i]], dp, hm)+c[i]
    ans = max(ans, helper(arr, c, i+1, n, k, dp, hm))
    dp[i][k] = ans
    return ans


def Solution(b, c, n, k, hm):
    # Write Your Code Here
    k = min(k, 12*n)
    dp = [[-1 for _ in range(k+1)] for _ in range(n)]
    # print(hm[31], hm[11])
    print(helper(b, c, 0, n, k, dp, hm))


def main():
    # Take input Here and Call solution function
    hm = [float("inf") for _ in range(1001)]
    hm[1] = 0
    for i in range(1, 1001):
        for x in range(1, i+1):
            j = i + (i // x)
            if (j <= 1000):
                hm[j] = min(hm[j], hm[i] + 1)

    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        b = get_ints_in_list()
        c = get_ints_in_list()
        Solution(b, c, n, k, hm)


# calling main Function
if __name__ == '__main__':
    main()
