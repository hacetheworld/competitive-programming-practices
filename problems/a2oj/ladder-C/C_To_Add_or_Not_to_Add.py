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

# -------- SOME CUSTOMIZED FUNCTIONS-----------


def myceil(x, y): return (x + y - 1) // y

# -------------- SOLUTION FUNCTION ------------------


def helper(arr, n, k, d, m):
    l = 0
    r = m
    ans = 0
    while l <= r:
        mid = (l+r)//2
        t = (m-mid)+1
        vl = arr[m] - (arr[mid-1] if mid > 0 else 0)
        # print("l", l, "r", r, "mid", mid, vl, "vl")
        if (t*d)-(k+(vl)) <= 0:
            # print("mid", mid)
            ans = mid
            r = mid-1
        else:
            l = mid+1
    # print("ans", ans, "m", m)
    return (m-ans)+1


def Solution(arr, n, k):
    # Write Your Code Here
    arr = sorted(arr)
    pf = [0]
    ans = -1
    el = -1
    # prev = -1
    for v in arr:
        pf.append(pf[-1]+v)
    pf.pop(0)
    for i in range(n):
        v = arr[i]
        res = helper(pf, n, k, v, i)
        if res > ans:
            el = v
            ans = res
    # print(pf)
    print(ans, el)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
