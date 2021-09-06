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


def swap(arr, i, j, swapped, op):
    while j >= 1 and op:
        if j in swapped and j-1 in swapped:
            return op
        if arr[j] > arr[j-1]:
            return op
        tmp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = tmp
        swapped[j-1] = True
        j -= 1
        op -= 1
    return op


def Solution(arr, n):
    # Write Your Code Here
    op = n-1
    i = 1
    swapped = {}
    while op and i <= n:
        smElIdx = arr.index(i)
        if not smElIdx in swapped and (smElIdx-1 >= 0 and not smElIdx-1 in swapped):
            op = swap(arr, 0, smElIdx, swapped, op)
        if op == 0:
            break
        i += 1
    print(*arr)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
