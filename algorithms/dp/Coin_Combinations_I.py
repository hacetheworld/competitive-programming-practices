# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout

# -------------- INPUT FUNCTIONS ------------------
# sys.setrecursionlimit(1000000)


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------------- SOLUTION FUNCTION ------------------


def Solution(arr, n, x):
    # Write Your Code Here
    mod = pow(10, 9)+7
    dp = [0 for _ in range(x+1)]
    dp[0] = 1
    for sm in range(1, x+1):
        for coin in arr:
            if coin > sm:
                continue
            dp[sm] = ((dp[sm] % mod)+(dp[sm-coin] % mod)) % mod
    print(dp[-1])


def main():
    # Take input Here and Call solution function
    n, x = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, x)


# calling main Function
if __name__ == '__main__':
    main()
