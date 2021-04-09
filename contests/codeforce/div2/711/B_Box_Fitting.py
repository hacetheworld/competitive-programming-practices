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


def binarySearchUpparBound(arr, key):
    left = 0
    right = len(arr)-1
    res = -1
    idx = 0
    while left <= right:
        mid = left+((right-left)//2)
        if arr[mid] <= key:
            left = mid+1
            res = arr[mid]
            idx = mid
        else:
            right = mid-1
    return (res, idx)


def Solution(arr, n, k):
    # Write Your Code Here
    arr = sorted(arr)
    ans = 0
    bits = [0 for _ in range(32)]
    for v in arr:
        x = int(math.log2(v))
        bits[x] += 1
    while n:
        tmp = k
        ans += 1
        i = 31
        while i >= 0 and tmp >= 0:
            if bits[i] > 0:
                val = pow(2, i)
                if (tmp-val) >= 0:
                    tmp -= val
                    bits[i] -= 1
                    n -= 1
                    i += 1
            i -= 1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, k = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, k)


# calling main Function
if __name__ == '__main__':
    main()
