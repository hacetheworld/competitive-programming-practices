# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
from bisect import bisect_right
from sys import stdin, stdout
# input = sys.stdin.buffer.readline

# -------------- INPUT FUNCTIONS ------------------


def get_ints_in_variables(): return map(
    int, sys.stdin.readline().strip().split())


def get_int(): return int(sys.stdin.readline())


def get_ints_in_list(): return list(
    map(int, input().split()))
def get_list_of_list(n): return [list(
    map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


def get_string(): return sys.stdin.readline().strip()

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def Solution(a, b, n):
    # Write Your Code Here
    prefixSum = [0]
    for i in range(n):
        prefixSum.append((prefixSum[-1]+a[i]*b[i]))
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n):
        for j in range(1, n+1):
            k = i+j
            if k > n:
                break
            dp[j][k] = a[j-1]*b[k-1]+a[k-1]*b[j-1]

            if j+1 <= k-1:
                if j+1 == k-1:
                    dp[j][k] += prefixSum[j+1]-prefixSum[j]
                else:
                    dp[j][k] += dp[j+1][k-1]
    ans = prefixSum[-1]
    # print(prefixSum)
    # print(dp)
    for i in range(1, n):
        for j in range(i+1, n+1):
            tmp = dp[i][j]
            if i-1 >= 1:
                tmp += prefixSum[i-1]
            if j+1 <= n:
                tmp += prefixSum[-1]-prefixSum[j]
            # print("i", i, "j", j, "tmp", tmp, "dp", dp[i][j])
            ans = max(ans, tmp)
            # print(ans, "ans")
    print(ans)


def main():
    # Take input Here and Call solution function
    n = get_int()
    a = get_ints_in_list()
    b = get_ints_in_list()
    Solution(a, b, n)


# calling main Function
if __name__ == '__main__':
    main()
