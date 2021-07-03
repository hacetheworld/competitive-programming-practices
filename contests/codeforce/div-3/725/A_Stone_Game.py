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


def Solution(arr, n):
    # Write Your Code Here
    mn = min(arr)
    mx = max(arr)
    ans = 0
    mnidx = -1
    mxidx = -1
    for i in range(n):
        if arr[i] == mn:
            mnidx = i+1
        if arr[i] == mx:
            mxidx = i+1
    if mnidx <= (n//2):
        ans += (mnidx)
    else:
        ans += (n-(mnidx-1))
    if mxidx <= (n//2):
        ans += (mxidx)
    else:
        ans += (n-(mxidx-1))
    ans = min(max(mnidx, mxidx), ans)
    ans = min(n-(min(mnidx, mxidx)-1), ans)
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
