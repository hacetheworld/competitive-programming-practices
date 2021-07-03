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


def isSorted(arr, n):
    p = 1
    for i in range(n):
        if arr[i] == p:
            p += 1
        else:
            return False
    return True


def Solution(arr, n):
    # Write Your Code Here
    if isSorted(arr, n):
        print(0)
    else:
        smidx = arr.index(1)
        mxidx = arr.index(n)

        if smidx == 0 or mxidx == n-1:
            print(1)
        elif smidx == n-1 and mxidx == 0:
            print(3)
        else:
            print(2)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
