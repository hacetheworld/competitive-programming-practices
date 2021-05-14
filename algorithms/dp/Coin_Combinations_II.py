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


def coinCombination(arr, n, x, sm, leftCoin, mod):
    if x == sm:
        return 1
    if sm > x or leftCoin <= 0:
        return 0
    ans = 0
    for i in range(leftCoin):
        ans += (coinCombination(arr, n, x, sm+arr[i], leftCoin, mod) % mod)+(
            coinCombination(arr, n, x, sm, leftCoin-1, mod) % mod) % mod
    return ans


def Solution(arr, n, x):
    # Write Your Code Here
    mod = pow(10, 9)+7
    res = coinCombination(arr, n, x, 0, n, mod)
    print(res)


def main():
    # Take input Here and Call solution function
    n, x = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, x)


# calling main Function
if __name__ == '__main__':
    main()
