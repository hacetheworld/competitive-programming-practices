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


def Solution(arr, n):
    dp = [[-1, - 1, - 1] for _ in range(n)]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[0][1]
    dp[0][2] = arr[0][2]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])+arr[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2])+arr[i][1]
        dp[i][2] = max(dp[i-1][1], dp[i-1][0])+arr[i][2]
    print(max(dp[-1]))


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
