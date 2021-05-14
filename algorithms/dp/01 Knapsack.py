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


def Knapsack(values, weights, w, n, i, dp):
    if i < 0 or w <= 0:
        return 0
    if dp[i][w] != -1:
        return dp[i][w]
    ans = 0
    if weights[i] <= w:
        ans = max(values[i]+Knapsack(values, weights, w-weights[i],
                                     n, i-1, dp), Knapsack(values, weights, w, n, i-1, dp))
    else:
        ans = Knapsack(values, weights, w, n, i-1, dp)
    dp[i][w] = ans
    return ans


def Solution():
    # Write Your Code Here
    n = get_int()
    values = get_ints_in_list()
    weights = get_ints_in_list()
    w = get_int()
    dp = [[-1 for _ in range(w+1)] for _ in range(n+1)]
    Knapsack(values, weights, w, n, n-1, dp)
    print(dp[n-1][w])


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
