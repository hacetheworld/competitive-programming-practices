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
    t, k = get_ints_in_variables()
    mod = pow(10, 9)+7
    dp = [0 for _ in range(pow(10, 5)+5)]
    dp[0] = 1
    for i in range(1, pow(10, 5)+1):
        if i < k:
            dp[i] = dp[i-1] % mod
        else:
            dp[i] = ((dp[i-1] % mod)+(dp[i-k] % mod)) % mod

    prefix = [0]

    for v in dp:
        prefix.append(((prefix[-1] % mod)+(v % mod)) % mod)
    prefix.pop(0)

    for _ in range(t):
        a, b = get_ints_in_variables()
        print((((prefix[b]-prefix[a]))+dp[a]) % mod)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
