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


# def helper(arr, i, prev, l, r, ql, qr, left, right):
#     if i >= len(arr):
#         return left+right
#     tmp = 0
#     vl = left
#     if prev == "l":
#         vl += ql
#     tmp = helper(arr, i+1, "l", l, r, ql, qr, vl+(arr[i]*l), right)
#     vr = right
#     if prev == "r":
#         vr += qr
#     tmp = min(tmp, helper(arr, i+1, "r", l, r, ql, qr, left, vr+(arr[i]*r)))
#     return tmp


def Solution(arr, n, l, r, ql, qr):
    # Write Your Code Here
    ans = float("inf")
    pref = [0]
    suff = [0]
    for v in arr:
        pref.append(pref[-1]+v)
    for i in range(n-1, -1, -1):
        suff.append(suff[-1]+arr[i])
    # pref.pop(0)
    # suff.pop(0)
    # suff = list(reversed(suff))
    for i in range(n+1):
        curr = (pref[i]*l)+(suff[n-i]*r)
        if i > (n-i):
            curr += ((2*i)-n-1)*ql
        if i < (n-i):
            curr += (n-(2*i)-1)*qr
        ans = min(ans, curr)
    print(ans)


def main():
    # Take input Here and Call solution function
    n, l, r, ql, qr = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, l, r, ql, qr)


# calling main Function
if __name__ == '__main__':
    main()
