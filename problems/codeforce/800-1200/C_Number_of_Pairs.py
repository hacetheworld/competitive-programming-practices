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


def bsRight(arr, n, l, r, rng):
    i = rng+1
    j = n-1
    ans = -1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] >= l and arr[mid] <= r:
            ans = mid
            i = mid+1
        elif arr[mid] > r:
            j = mid-1
        else:
            i = mid+1
    return ans


def bsLeft(arr, n, l, r, rng):
    i = rng+1
    j = n-1
    ans = -1
    while i <= j:
        mid = (i+j)//2
        if arr[mid] >= l and arr[mid] <= r:
            ans = mid
            j = mid-1
        elif arr[mid] > r:
            j = mid-1
        else:
            i = mid+1
    return ans


def Solution(arr, n, l, r):
    # Write Your Code Here
    arr = sorted(arr)
    ans = 0
    for i in range(n-1):
        left = bsLeft(arr, n, l-arr[i], r-arr[i], i)
        # print("left", left)
        right = bsRight(arr, n, l-arr[i], r-arr[i], i)
        # print("right", right)
        if left != -1 and right != -1:
            ans += (right-left)+1
        # print("ans", ans)
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, l, r = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, l, r)


# calling main Function
if __name__ == '__main__':
    main()
