# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# -------- IMPORTANT ---------#
# SUN BHOS**KE AGAR MERA TEMPLATE COPY KAR RHA HAI NA TOH KUCH CHANGES BHI KAR DENA ESS ME, VARNA MUJEHY WARNING AAYEGI BAAD ME, PLEASE YAAR KAR DENA, OK :).
import sys
import bisect
from bisect import bisect_right

import math
from sys import stdin, stdout


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def helper(arr, n, day, i, dp):
    if day >= n:
        return 0
    if dp[day][i] != -1:
        return dp[day][i]
    for j in range(3):
        if j == i:
            continue
        dp[day][j] = arr[day][j]+helper(arr, n, day+1, j, dp)
    return dp[day][i]


def Solution(arr, n):
    dp = [[-1, - 1, - 1] for _ in range(n)]
    for i in range(3):
        dp[0][i] = arr[0][i]+helper(arr, n, 1, i, dp)
    print(dp)
    print(max(dp[0]))


def main():
    # //Write Your Code Here
    n = get_int()
    arr = []
    for _ in range(n):
        pair = get_ints_in_list()
        arr.append(pair)
    Solution(arr, n)


#  calling main Function
if __name__ == "__main__":
    main()
