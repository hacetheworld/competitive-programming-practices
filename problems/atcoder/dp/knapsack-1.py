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


def Solution(arr, n, w):
    # Write Your Code Here
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if arr[i-1][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-arr[i-1][0]]+arr[i-1][1], dp[i-1][j])
    print(dp[n][w])


def main():
    # Take input Here and Call solution function
    n, w = get_ints_in_variables()
    arr = []
    for _ in range(n):
        item = get_ints_in_list()
        arr.append(item)
    Solution(arr, n, w)


# calling main Function
if __name__ == '__main__':
    main()
