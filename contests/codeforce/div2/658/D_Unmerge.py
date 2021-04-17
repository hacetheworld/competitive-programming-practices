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


def nextGreaterEl(hm, el, n):
    for i in range(el+1, n+1):
        if not i in hm:
            return i


def Solution(arr, n):
    # Write Your Code Here
    subsets = []
    i = 0
    n1 = 2*n
    while i < n1:
        el = arr[i]
        length = 1
        i += 1
        while i < n1 and el > arr[i]:
            length += 1
            i += 1
        subsets.append(length)
    # print(subsets)
    dp = [[0 for _ in range(n+1)] for _ in range(len(subsets)+1)]
    dp[0][0] = 1
    for i in range(1, len(subsets)+1):
        dp[i][0] = 1
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if j >= subsets[i-1]:
                dp[i][j] |= dp[i-1][j-subsets[i-1]]
    # print(dp)
    if dp[len(subsets)][n]:
        print("YES")
    else:
        print("NO")


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
