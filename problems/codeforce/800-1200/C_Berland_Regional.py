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


def Solution(uArr, sArr, n):
    # Write Your Code Here
    hm = {}
    for i in range(n):
        if uArr[i] in hm:
            hm[uArr[i]].append(sArr[i])
        else:
            hm[uArr[i]] = [sArr[i]]
    for u in hm:
        hm[u] = sorted(hm[u])
    dp = [0 for _ in range(n+1)]
    for u in hm:
        prevSum = [0]
        m = len(hm[u])
        for i in range(m-1, -1, -1):
            prevSum.append(prevSum[-1]+hm[u][i])
        for i in range(1, m+1):
            dp[i] += prevSum[m-(m % i)]
    for i in range(1, n+1):
        print(dp[i], end=" ")
    print()


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        arr2 = get_ints_in_list()
        Solution(arr, arr2, n)


# calling main Function
if __name__ == '__main__':
    main()
