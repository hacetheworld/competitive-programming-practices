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


def check(arr, n, k):
    for i in range(n):
        if arr[i] == 0:
            k += 1
        if arr[i] > k:
            return False
    return True


def Solution(a, b, k, n, m):
    # Write Your Code Here
    res = []
    i = 0
    j = 0

    while i < n and j < m:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < n:
        res.append(a[i])
        i += 1
    while j < m:
        res.append(b[j])
        j += 1
    if check(res, n+m, k):
        print(*res)
    else:
        print(-1)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        input()
        k, n, m = get_ints_in_variables()
        a = get_ints_in_list()
        b = get_ints_in_list()
        Solution(a, b, k, n, m)


# calling main Function
if __name__ == '__main__':
    main()
