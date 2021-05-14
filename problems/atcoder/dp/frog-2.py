# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638

# -------- IMPORTANT ---------#
# SUN BHOS**KE AGAR MERA TEMPLATE COPY KAR RHA HAI NA TOH KUCH CHANGES BHI KAR DENA ESS ME, VARNA MUJEHY WARNING AAYEGI BAAD ME, PLEASE YAAR KAR DENA, OK :).
import sys
import bisect
from bisect import bisect_right

import math
from sys import stdin, stdout

# //Most Frequently Used Number Theory Concepts
# VAISE MEIN JAYDA USE KARTA NHI HU ENHE BUT COOL BANNE KE LIYE LIKH LEYA TEMPLATE ME VARNA ME YE TOH DUSRI FILE MAI SE BHI COPY PASTE KAR SAKTA THA :).


def get_ints_in_variables():
    return map(int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()


def Solution(arr, n, k):
    dp = [float("inf") for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, k+1):
            if i-j < 0:
                break
            dp[i] = min(dp[i], abs(arr[i]-arr[i-j])+dp[i-j])

    print(dp[-1])


def main():
    # //Write Your Code Here
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


#  calling main Function
if __name__ == "__main__":
    main()
