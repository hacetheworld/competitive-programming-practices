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


def bst(arr, n, key):
    i = 0
    j = n-1
    ans = -1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] <= key:
            i = mid+1
            ans = mid
        else:
            j = mid-1
    return ans


def Solution(arr, n, m):
    # Write Your Code Here
    up = [i for i in range(n)]
    dw = [i for i in range(n)]
    for i in range(1, n):
        if arr[i] <= arr[i-1]:
            up[i] = up[i-1]
    for i in range(n-2, -1, -1):
        if arr[i] <= arr[i+1]:
            dw[i] = dw[i+1]
    for _ in range(m):
        l, r = get_ints_in_variables()
        if up[r-1] <= dw[l-1]:
            print("Yes")
        else:
            print("No")


def main():
    # Take input Here and Call solution function
    n, m = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, m)


# calling main Function
if __name__ == '__main__':
    main()
