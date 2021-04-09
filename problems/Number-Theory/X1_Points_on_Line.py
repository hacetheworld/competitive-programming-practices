# Author Name: Ajay Meena
# Codeforce : https://codeforces.com/profile/majay1638
import sys
import math
import bisect
import heapq
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


def binarySearchUpparBound(arr, key, l):
    left = l
    right = len(arr)-1
    res = -1
    while left <= right:
        mid = left+((right-left)//2)
        if arr[mid] <= key:
            left = mid+1
            res = mid
        else:
            right = mid-1
    return res


def Solution(arr, n, d):
    # Write Your Code Here
    res = 0
    for i in range(n-2):
        t = arr[i]
        m = binarySearchUpparBound(arr, t+d, i)-i
        if m != -1:
            res += ((m*(m-1))//2)
    print(res)


def main():
    # Take input Here and Call solution function
    n, d = get_ints_in_variables()
    arr = get_ints_in_list()
    Solution(arr, n, d)


# calling main Function
if __name__ == '__main__':
    main()
