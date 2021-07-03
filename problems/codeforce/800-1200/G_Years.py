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


def countLeft(arr, s, e, itm):
    l = s
    r = e
    tmp = 0
    while l <= r:
        mid = (l+r)//2
        midItm = arr[mid]
        if itm[1] > midItm[0]:
            pass


def countRight(arr, s, e, itm):
    pass


def Solution():
    # Write Your Code Here
    n = get_int()
    arr = [get_ints_in_list() for _ in range(n)]
    arr = sorted(arr, key=lambda x: x[0])
    ans = []
    for i in range(n):
        itm = arr[i]
        left = countLeft(arr, 0, i, itm)
        right = countRight(arr, i+1, n, itm)
        ans = max(ans, left+right+1)
    print(ans)


def main():
    # Take input Here and Call solution function
    Solution()


# calling main Function
if __name__ == '__main__':
    main()
