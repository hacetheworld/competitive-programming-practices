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


def checkBit(bits, k):
    count = 0
    for i in range(len(bits)-1):
        if bits[i] == "1" and bits[i+1] == "1":
            count += 1
    return 1 if k == count else 0


def adjacentBitCount(res, n, k, i, dp):
    if i >= n:
        return 0
    if dp[i] != -1:
    return dp[i]
    res.append("1")
    dp[i] = adjacentBitCount(res, n, k, i+1, dp)

    res[i] = "0"
    dp[i] += adjacentBitCount(res, n, k, i+1, dp)
    return dp[i]


def Solution(t, n, k):
    # Write Your Code Here
    res = []
    dp = [-1 for _ in range(n)]
    adjacentBitCount(res, n, k, 0, dp)
    print(dp)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        t, n, k = get_ints_in_variables()
        Solution(t, n, k)


# calling main Function
if __name__ == '__main__':
    main()
