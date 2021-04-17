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
    k, l, m = get_ints_in_variables()
    arr = get_ints_in_list()
    dp = [0 for _ in range(m+1)]
    dp[1] = 1
    for i in range(m):
        dp[i+1] = dp[i-1]
        if arr[i] >= k:
            d[i+1] = dp[i+1] or dp[i-k]
        if i >= l:
            d[i+1] = dp[i+1] or dp[i-l]
    print(dp)



def main():
    # Take input Here and Call solution function
    pass


# calling main Function
if __name__ == '__main__':
    main()
