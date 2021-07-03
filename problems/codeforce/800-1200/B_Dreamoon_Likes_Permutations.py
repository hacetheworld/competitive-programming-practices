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


def check(arr, n, mx):
    hm = {}
    for i in range(mx):
        if arr[i] in hm:
            hm[arr[i]] += 1
        else:
            hm[arr[i]] = 1
    for i in range(1, mx+1):
        if not i in hm:
            return False
    s = {}
    for i in range(mx, n):
        if arr[i] in s:
            s[arr[i]] += 1
        else:
            s[arr[i]] = 1
    for i in range(1, (n-mx)+1):
        if not i in s:
            return False
    return True


def Solution(arr, n):
    # Write Your Code Here
    res = set()
    mx = max(arr)

    if check(arr, n, mx):
        res.add((mx, n-mx))
    if check(arr, n, n-mx):
        res.add((n-mx, mx))
    print(len(res))
    for v in res:
        print(*v)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
