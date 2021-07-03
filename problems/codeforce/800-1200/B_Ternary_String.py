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


def bsrchright(arr, n, key):
    l = 0
    r = n-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] < key:
            l = mid+1
        else:
            ans = arr[mid]
            r = mid-1
    return ans


def bsrch(arr, n, key):
    l = 0
    r = n-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] > key:
            r = mid-1
        else:
            ans = arr[mid]
            l = mid+1
    return ans


def Solution(s, n):
    # Write Your Code Here
    ans = float("inf")
    i, j, k = -1, -1, -1
    for l in range(n):
        c = s[l]
        if c == "1":
            i = l
        elif c == "2":
            j = l
        else:
            k = l
        if i != -1 and j != -1 and k != -1:
            ans = min(ans, abs(min([i, j, k])-max([i, j, k])))

    if ans != float("inf"):
        print(ans+1)
    else:
        print(0)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        s = get_string()
        Solution(s, len(s))


# calling main Function
if __name__ == '__main__':
    main()
