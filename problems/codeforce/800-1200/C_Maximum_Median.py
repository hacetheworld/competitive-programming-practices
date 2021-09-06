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


def check(arr, n, x, k):
    sm = 0
    for i in range(n//2, n):
        if x-arr[i] > 0:
            sm += x-arr[i]
        if sm > k:
            return False
    return True


def Solution(arr, n, k):
    # Write Your Code Here
    arr = sorted(arr)

    l = arr[n//2]
    r = (l)+k
    ans = 0
    while l <= r:
        mid = (l+r)//2
        if check(arr, n, mid, k):
            l = mid+1
            ans = mid
        else:
            r = mid-1
    print(ans)


def main():
    # Take input Here and Call solution function
    n, k = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
