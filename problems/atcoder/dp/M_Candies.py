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


def Solution():
    # Write Your Code Here
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    arr.insert(0, 0)
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(k+1):
        dp[1][i] = 0 if i > arr[1] else 1
    mod = pow(10, 9)+7
    for i in range(2, n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (mod+(((dp[i][j-1] % mod)+(dp[i-1][j] % mod))) - (dp[i-1]
                                                                             [j-arr[i]-1] % mod if ((j-arr[i]-1) >= 0) else 0)) % mod
    # print(dp)
    print(dp[n][k])


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
