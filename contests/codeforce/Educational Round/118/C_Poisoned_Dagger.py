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


def check(arr, n, x, h):
    tmp = 0
    for i in range(n-1):
        tmp += (min(x, arr[i+1]-arr[i]))
    tmp += x
    if tmp >= h:
        return True
    else:
        return False


def Solution(arr, n, h):
    # Write Your Code Here
    l = 1
    r = h
    ans = h
    while l <= r:
        md = (l+r)//2
        if check(arr, n, md, h) and md < ans:
            ans = md
            r = md-1
        else:
            l = md+1
    print(ans)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n, h = get_ints_in_variables()
        arr = get_ints_in_list()
        Solution(arr, n, h)


# calling main Function
if __name__ == '__main__':
    main()
