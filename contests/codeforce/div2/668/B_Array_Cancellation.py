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


def Solution(arr, n):
    # Write Your Code Here
    ans = 0
    for v in arr:
        if v > 0:
            ans += v
    tmp = 0
    neg = ans
    taken = 0
    for v in arr:
        # print(neg, "neg")
        if v < 0:
            neg -= 0 if taken >= abs(v) else abs(v)-taken
            taken = taken-abs(v)
            if taken < 0:
                taken = 0
        else:
            t = (min(v, neg))
            taken += t
            tmp += t
            neg -= t
        if neg <= 0:
            break
    print(ans-tmp)


def main():
    # Take input Here and Call solution function
    for _ in range(get_int()):
        n = get_int()
        arr = get_ints_in_list()
        Solution(arr, n)


# calling main Function
if __name__ == '__main__':
    main()
